from django import forms
from django.db import models
from django.contrib.auth import authenticate



class LoginForm(forms.Form):

    user = forms.CharField(
        label="Usuario ",
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Usuario...'
            }
        )
    )
    password = forms.CharField(
        label="Contraseña ",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña...'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        user = self.cleaned_data['user']
        password = self.cleaned_data['password']

        if not authenticate(username=user, password=password):
            raise forms.ValidationError('El usuario y/o la contraseña son incorrectos')
        
        return cleaned_data