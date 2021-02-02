from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email'}, max_length=64, label="Email")
    password = forms.CharField(error_messages={
        'required': 'Please enter your password'}, widget=forms.PasswordInput, label="Password")
    con_password = forms.CharField(error_messages={
        'required': 'Please enter your password again'}, widget=forms.PasswordInput, label="Password Confirm")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        con_password = cleaned_data.get('con_password')
        email_check = User.objects.get(email=email)

        if email_check:
            self.add_error('email', 'This email is already registered')

        if password and con_password:
            if password != con_password:
                self.add_error('password', 'Password is not matched')
                self.add_error('con_password', 'Password is not matched')


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email'}, max_length=64, label="Email")
    password = forms.CharField(error_messages={
        'required': 'Please enter your password'}, widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', 'This email is not registered')
                return

            if not check_password(password, user.password):
                self.add_error('password', 'Password is not correct')
