from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    msg = forms.CharField(widget=forms.TextInput())