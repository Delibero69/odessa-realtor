# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)

# class ContactFormsTwo(forms.Form):
#     name = forms.CharField(max_length=100)
#     phone_number = forms.CharField(max_length=15)
#     content = forms.TextField()


class ContactForm2(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    content = forms.CharField(widget=forms.Textarea)
