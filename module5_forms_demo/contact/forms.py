from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Message',
        }

        widgets = {
            'message': forms.Textarea(),
        }