from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_user.models import BloodGroups, Roles

from .models import User
from .serializers import (BloodGroupsSerializer, ChangePasswordSerializer,
                          LoginSerializer, RolesSerializer, SignupSerializer,
                          UserObjectSerializer)
from .utils import get_token_for_user

# Create your views here.


class SignupAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserObjectSerializer(user).data, status=201)


class BloodGroupsListAPIView(ListAPIView):
    serializer_class = BloodGroupsSerializer
    queryset = BloodGroups.objects.all()


class RolesListAPIView(ListAPIView):
    serializer_class = RolesSerializer
    queryset = Roles.objects.all()


class LoginAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            email=serializer.validated_data.get('email'),
            password=serializer.validated_data.get('password')
        )
        if user:
            token = get_token_for_user(user)
            data = UserObjectSerializer(user).data
            data['token'] = {
                'access': token.key
            }
            return Response(data)
        raise AuthenticationFailed('Bad Credentials')


class ChangePasswordAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = ChangePasswordSerializer(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()

    def get_serializer_context(self) -> dict:
        context = {
            'request': self.request
        }
        return context
