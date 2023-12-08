from django import forms
from django.contrib.auth.forms import UsernameField,UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer, ReviewRating


class LoginForm(AuthenticationForm):
   username=UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput (attrs={'autocomplete':'current-password','class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True',                                                     'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class MyPasswordChange(PasswordChangeForm):
    old_password =forms.CharField(label='Old Password',widget = forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 =forms.CharField(label='New Password',widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 =forms.CharField(label='Confirm Password',widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields =['name','address','mobile']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
             'address':forms.TextInput(attrs={'class':'form-control'}),
              'mobile':forms.NumberInput(attrs={'class':'form-control'})
        }
class MyPasswordResetForm(PasswordResetForm):
    new_password1 =forms.CharField(label='New Password',widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 =forms.CharField(label='Confirm Password',widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating  # Replace with your actual Review model
        fields = ['review', 'rating']  # Add other fields as needed