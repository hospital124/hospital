from django import forms
from .models import doctor
from django.contrib.auth.models import User
class patientsearchform(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Search'}))