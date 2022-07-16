from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import *
app_name = 'STARTUP'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutView.as_view(), name='about'),
    path('services/', ServiesView.as_view(), name='services'),
    path('contact-us/', ContactView.as_view(), name='contact'),
    path('project/<slug:slug>/', Project_Done_Details.as_view(), name='project_done_details'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

