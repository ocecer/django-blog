from dataclasses import field
from django import forms
from blog.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('fullName', 'email', 'message')
