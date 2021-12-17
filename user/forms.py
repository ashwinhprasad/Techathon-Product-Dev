from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6,widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model= UserModel
        fields = ('email','username','password','confirm_password',
        'phone')
        

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('confirm_password')

        if pass1 != pass2:
            print("error")
            raise forms.ValidationError('Passwords do not match')