from django.contrib.auth.models import User


class EmailAuthBackend:
    """ Аутентификация посредством адреса электронной почты """
    def authenticate(self, request, username=None, password=None):
        """ Извлекаем пользователя с заданным адресом электронной почты """
        try:
            user = User.objects.get(username=username)
            # Проверяем пароль
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        """ Извлекаем пользователя по ID """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
