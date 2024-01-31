# models.py

# models.py
from django.db import models

class InsuranceResult(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.FloatField()
    smoker = models.CharField(max_length=3)
    region = models.CharField(max_length=10)
    children = models.IntegerField()
    predicted_insurance_charge = models.FloatField()



from django import forms

class ContactForm(models.Model):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact_number = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
