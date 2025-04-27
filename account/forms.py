from django import forms
from django.contrib.auth import get_user_model

from account.models import Profile


class LoginForm(forms.Form):
    """ Форма аутентификации пользователя """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """ Форма регистрации пользователя """
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        """ Проверяет совпадение паролей внесенных в password и password2 """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    """ Форма для редактирования имени, фамилии, e-mail """
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    """ Форма для редактирования данных профиля """
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
