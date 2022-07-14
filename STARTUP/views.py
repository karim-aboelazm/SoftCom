from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home_pages/index.html'

class AboutView(TemplateView):
    template_name = 'about_us_pages/about_us.html'


class ServiesView(TemplateView):
    template_name = 'services_pages/services.html'

class ContactView(TemplateView):
    template_name = 'contact_pages/contact_us.html'

