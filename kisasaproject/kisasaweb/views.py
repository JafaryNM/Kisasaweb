from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexTemplate(TemplateView):
    template_name='index.html'

class BaseTemplate(TemplateView):
    template_name= 'base.html'

class AboutPage(TemplateView):
    template_name='about.html'

class ContactUs(TemplateView):
    template_name="contact.html"

class ServicesPage (TemplateView):
    template_name='services.html'