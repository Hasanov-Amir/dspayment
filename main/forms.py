from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["cc_number", "cc_holder_name", "cc_expiry", "cc_code"]
