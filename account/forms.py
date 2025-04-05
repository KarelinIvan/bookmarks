from django import forms


class LoginForm(forms.Form):
    """ Форма для аутентификации пользователей """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
