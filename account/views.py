from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from account.forms import LoginForm


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
