from oscar.apps.customer.views import AccountAuthView as BaseAccountAuthView
from oscar.apps.customer.views import AccountRegistrationView as BaseAccountRegistrationView
from oscar.core.loading import get_class

from .forms import UserCreationForm


class AccountAuthView(BaseAccountAuthView):
    registration_form_class = UserCreationForm

class AccountRegistrationView(BaseAccountRegistrationView):
    form_class = UserCreationForm
