from django import forms
from django.contrib.auth.models import User

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
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        """ Проверяет совпадение паролей внесенных в password и password2 """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        """ Валидация электронной почты, которая не позволяет пользователям
        регистрироваться с уже существующим адресом электронной почты """
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Электронная почта уже используется')
        return data


class UserEditForm(forms.ModelForm):
    """ Форма для редактирования имени, фамилии, e-mail """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        """ Валидация поля email, чтобы пользователи не могли изменить свой адрес электронной почты
         на существующий адрес электронной почты другого пользователя """
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Электронная почта уже используется')
        return data


class ProfileEditForm(forms.ModelForm):
    """ Форма для редактирования данных профиля """

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
