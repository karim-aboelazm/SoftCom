from django.views.generic import TemplateView,DetailView,ListView,FormView
from django.shortcuts import render
from .froms import ContactForm
from django.urls import reverse_lazy,reverse
from django.core.mail import send_mail
from django.conf import settings

from .models import *

class HomeView(TemplateView):
    template_name = 'home_pages/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["statistics"] = OurStatistics.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        context["cat_and_icon"] = zip(context["categories"],["ti-light-bulb","ti-panel","ti-search","ti-rocket"])
        context["project_done"] = Projects_had_done.objects.all().order_by('-pk')
        context["bg"] = Site_bg_Images.objects.latest('pk')
        return context

class AboutView(TemplateView):
    template_name = 'about_us_pages/about_us.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["teams"] = OurTeam.objects.all()
        context["statistics"] = OurStatistics.objects.latest('pk')
        context["rewards"]= Reward.objects.all()
        context["categories"] = Job_Categories.objects.all()
        context["bg"] = Site_bg_Images.objects.latest('pk')
        return context

class ServiesView(TemplateView):
    template_name = 'services_pages/services.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        context["services"] = Services.objects.all()
        context["work_steps"] = Work_Steps.objects.all()
        context["bg"] = Site_bg_Images.objects.latest('pk')
        return context

class ContactView(FormView):
    template_name = 'contact_pages/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('startup:contact')
    def form_valid(self,form):
        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data['email']
        msg = form.cleaned_data['msg']
        myemail = settings.EMAIL_HOST_USER
        send_mail(subject,msg,myemail,[email],fail_silently = False)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        context["pranches"] = Pranches.objects.all().order_by('pk')
        context["bg"] = Site_bg_Images.objects.latest('pk')
        return context

class Project_Done_DetailsView(TemplateView):
    template_name = 'project_done_pages/project_done_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_slug = kwargs['slug']
        context["project"] = Projects_had_done.objects.get(slug=project_slug)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all().order_by('-pk')
        context["bg"] = Site_bg_Images.objects.latest('pk')
        return context

class CategoryView(TemplateView):
    template_name = 'category_pages/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com"] = Company.objects.latest('pk')
        context["categories"] = Job_Categories.objects.all()
        context["bg"] = Site_bg_Images.objects.latest('pk')
        return context