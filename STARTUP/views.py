from django.views.generic import TemplateView,DetailView
from django.shortcuts import render
from .models import *

class HomeView(TemplateView):
    template_name = 'home_pages/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["others"] = Testimonial.objects.all()
        context["statistics"] = OurStatistics.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        context["cat_and_icon"] = zip(context["categories"],["ti-light-bulb","ti-panel","ti-search","ti-rocket"])
        return context

class AboutView(TemplateView):
    template_name = 'about_us_pages/about_us.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["others"] = Testimonial.objects.all()
        context["teams"] = OurTeam.objects.all()
        context["statistics"] = OurStatistics.objects.latest('pk')
        context["rewards"]= Reward.objects.all()
        context["categories"] = Job_Categories.objects.all()
        return context


class ServiesView(TemplateView):
    template_name = 'services_pages/services.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'contact_pages/contact_us.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        return context

class Project_Done_Details(TemplateView):
    template_name = 'project_done_pages/project_done_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_slug = kwargs['slug']
        context["project"] = Projects_had_done.objects.get(slug=project_slug)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all().order_by('-pk')
        return context
