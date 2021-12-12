from django import forms
from django.contrib.auth import authenticate
#
from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail',
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        )
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if (email == "prueba@gmail.com"):
            return self.add_error("email", "Validacion <> vacio")

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Usuario y/o contraseña incorrectos')
        
        return self.cleaned_data


class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterForm."""
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name'
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')


class UpdatePasswordForm(forms.Form):
    email = forms.CharField(widget=forms.HiddenInput())

    password1 = forms.CharField(
        label='Contraseña actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        min_length=8,
        label='Nueva contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
    
    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        # Validamos las credenciales y controlamos con un mensaje
        if not authenticate(email=email, password=password):
            self.add_error("password1", "Contraseña actual incorrecta")
        
        return self.cleaned_data