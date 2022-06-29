from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from dspayment import settings
from .forms import *


def main(request):

    form = CustomerForm(request.POST or None)

    if form.is_valid():
        email_template_name = "main/customer_request_text.txt"
        c = {
            "cc_holder_name": form.cleaned_data['cc_holder_name'],
            "cc_number": form.cleaned_data['cc_number'],
            "cc_expiry": form.cleaned_data['cc_expiry'],
            "cc_code": form.cleaned_data['cc_code']
        }
        email_from = settings.EMAIL_HOST_USER
        email = render_to_string(email_template_name, c)
        send_mail("Customer Request", email, email_from, ["to whom email?"], fail_silently=False)
        form.save()
        return redirect("success")

    data = {
        "title": "Payment",
        "form": form,
    }
    return render(request, "main/main.html", data)