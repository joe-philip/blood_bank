from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignupSerializer, UserObjectSerializer

# Create your views here.


class SignupAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserObjectSerializer(user).data, status=201)
