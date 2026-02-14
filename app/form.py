from django import forms

class student_registration(forms.Form):
    name   = forms.CharField()
    email  = forms.EmailField()
    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# All the Function in UserCreationForm is Added to the Signupform
# class Signupform(UserCreationForm):
#     class Meta:
#         fields = ['Username', 'First name', 'Last name', 'Email address']