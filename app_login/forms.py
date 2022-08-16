from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from .models import Register

# class RegisterModelForm(forms.ModelForm):
#     GENDER_CHOICES = [('M','Male'),('F','Female'), ('O', 'Other')]
#     gender = forms.CharField(
#         label='Gender:',
#         required=True,
#         widget=forms.RadioSelect(choices=GENDER_CHOICES)
#     )
#     password = forms.CharField(
#         label='Password:',
#         required=True,
#         widget=forms.PasswordInput()
#     )
    
#     class Meta:
#         model = Register
#         fields = ['fullname', 'email', 'username', 'password', 'gender']
#         labels = {
#             'username': 'Username:',
#             'password': 'Password:',
#             'fullname': 'Fullname:',
#             'email': 'Email:',
#             'gender': 'Gender:'
#         }

# Register form
class RegisterModelForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password:',
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirm password:',
        required=True,
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'password1': 'Password:',
            'password2': 'Confirm password:'
        }

# Login form
class LoginModelForm(forms.ModelForm):
    password = forms.CharField(
        label='Password:',
        required=True,
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Username:',
            'password': 'Password:'
        }
