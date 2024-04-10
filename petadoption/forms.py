from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Animal, Adopter

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1']


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopter
        fields = ['name', 'email', 'phone_number', 'address']
        
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'breed', 'age', 'description', 'image']

