from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings


def run():
    if User.objects.all().count() == 0:
        user = User()
        user.username = "api_user"
        user.set_password(settings.API_USER_PASS)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        user.refresh_from_db()

        token = Token()
        token.user = user
        token.key = settings.API_USER_TOKEN
        token.save()
