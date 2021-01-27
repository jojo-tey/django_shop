from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=64, label='Email')

    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    re_password = forms.CharField(
        widget=forms.PasswordInput, label='Re_password')


# error_messages={
#             'required': 'Enter your email address'
#         },

#         error_message={
#         'required': 'Enter your password'
#     },


#     error_message={
#         'required': 'Enter your password again'
#     },
