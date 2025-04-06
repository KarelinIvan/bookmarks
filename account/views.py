from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from account.forms import LoginForm, UserRegistrationForm


def user_login(request):
    """ Функция для входа в учётную запись """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация прошла успешно')
                else:
                    return HttpResponse('Отключенная учетная запись')
            else:
                return HttpResponse('Неверный логин или пароль!')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    """ Проверяет аутентификацию текущего пользователя. Если пользователь аутентифицирован, то он исполняет
    декорированное представление; если нет, то перенаправляет на url входа в учётную запись """
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    """ Функция для регистрации нового пользователя """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаём новый объект пользователя, но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Устанавливаем выбранный пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем объект User
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
