from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import gettext as _


class Customer(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_holder_name = models.CharField(max_length=100, verbose_name="Name")
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.cc_holder_name}"
