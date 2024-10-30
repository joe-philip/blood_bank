from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_user.models import BloodGroups

from .serializers import (BloodGroupsSerializer, SignupSerializer,
                          UserObjectSerializer)

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
