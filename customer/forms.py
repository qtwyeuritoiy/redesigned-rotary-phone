from django import forms
from django.contrib.auth.models import Permission

from oscar.apps.customer.forms import EmailUserCreationForm
from oscar.apps.partner.models import Partner

from oscar_accounts import models, codes, names

class UserCreationForm(EmailUserCreationForm):
    partner_check = forms.BooleanField(label='I want to sell items', required=False)

    def __init__(self, host=None, *args, **kwargs):
        super().__init__(host=None, *args, **kwargs)
        print("__init__")

    def save(self, commit=True):
        is_partner = self.cleaned_data.get('partner_check', False)
        user = super().save()

        account_type = models.AccountType.objects.get(name=names.DEFERRED_INCOME)

        user_account = models.Account.objects.create(primary_user=user, credit_limit=None)
        user_account.code = codes.generate()
        user_account.account_type = account_type
        user_account.save()

        if is_partner:
            partner = Partner.objects.create(name=user.email)
            partner.users.add(user)
            partner.save()

            dashboard_access_perm = Permission.objects.get(
                codename='dashboard_access', content_type__app_label='partner')
            user.user_permissions.add(dashboard_access_perm)
        return user
