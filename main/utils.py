from rest_framework.authtoken.models import Token

from .models import User


def get_token_for_user(user: User) -> Token:
    if (token := Token.objects.filter(user=user)).exists():
        token.delete()
    return Token.objects.create(user=user)
