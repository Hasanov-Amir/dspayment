from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('success/', TemplateView.as_view(template_name="main/success.html"), name="success")
]
