from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class DropdownMenuForm(forms.Form):
    brushType = forms.CharField(max_length=10, help_text="Enter the type of brush: ")

class updateCompValueForm(forms.Form):
    component = forms.ChoiceField(label = False, choices=
        [(0, 'Select'), (1, 'Curtain'), (2, 'Rocker Brush'),
         (3, 'Wrap Brush'), (4, 'Side Brush'),
         (5, 'Takeup Drum'), (6, 'Sprocket'),
         (7, 'Fork Cover'), (8, 'Fork Cylinder'),
         (9, 'Heco Drive'), (10, 'Conveyor Hydraulic Motor'),
         (11, 'Chain/Rollers'), (12, "All Brushes"), (13, "All Components")], widget=forms.Select(
             attrs={'class' : 'dropdownMenu'}
         ))
