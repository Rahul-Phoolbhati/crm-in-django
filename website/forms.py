from django import form
from django.contrib.auth.models import User #aloows us to create superuser
from django.contrib.auth.forms import UserCreationForm #creates users
from .models import Record

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='email',required, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    #as bootstarp is used to design it , so botttsrap needs class 
    #The attrs parameter within widget allows you to set the HTML attributes, such as class for styling and placeholder for a placeholder text.
    first_name=forms.CharField(label='First Name', max_length=100,required,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name=forms.CharField(label='Last Name', max_length=100,required,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
