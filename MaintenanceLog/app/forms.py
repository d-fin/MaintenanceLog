from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class DropdownMenuForm(forms.Form):
    brushType = forms.CharField(max_length=10, help_text="Enter the type of brush: ")
