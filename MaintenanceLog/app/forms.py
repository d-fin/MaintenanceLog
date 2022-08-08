from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Maintenance
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

class updateTimeForm(forms.Form):
    id = forms.IntegerField()
    time = forms.ChoiceField(label=False,
        choices = [
            (0, "Select time to update"),
            (1, "3 Months"),
            (2, "6 Months"),
            (3, "9 Months"),
            (4, "1 Year")
        ],
        widget=forms.Select(
            attrs={'class' : 'timeDropDown',
                    'name' : 'timeBtn',
                    'onChange' : 'form.submit()'
                }
        )
    )

class editProfileForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(
             attrs={'class' : 'text-box-form',
                    'placeholder' : 'Full name' 
                }
    ))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
             attrs={'class' : 'text-box-form',
                    'placeholder' : 'Email'
             }
    ))
    username = forms.CharField(label="Username", max_length=20, widget=forms.TextInput(
             attrs={'class' : 'text-box-form',
                'placeholder' : 'Username'
             }
    ))
    site = forms.ChoiceField(label=False, 
        choices=[
            (0, "Select a primary site"),
            (1, "Gull Rd."),
            (2, "Stadium Dr.")
        ], 
        widget=forms.Select(
             attrs={'class' : 'dropdownMenu'}
    ))

""" class textAreaForm(forms.Form):
    notes = forms.CharField(label=False,
        widget=forms.Textarea(
            attrs={'class' : 'notesTextArea',
                'rows' : 5,
                'cols' : 50 
            }
        )
    )
    class Meta:
        model = Maintenance
        fields = ['notes'] """