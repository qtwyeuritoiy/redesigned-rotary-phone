from django import forms
from oscar.apps.customer.forms import EmailUserCreationForm
from partner.models import Partner

class PartnerForm(forms.ModelForm):
    pass


from oscar.apps.customer.forms import *  # noqa isort:skip
