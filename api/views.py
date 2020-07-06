import re

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework_jwt.serializers import jwt_encode_handler
# from rest_framework_jwt.serializers import jwt_payload_handler

from api.models import User
from api.serializers import UserModelSerializer
from utils.response import APIResponse
# from api.authentication import JWTAuthentication


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    # authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        return APIResponse(results={"username": request.user.username})


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)

        return APIResponse(data_message="ok", token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)
