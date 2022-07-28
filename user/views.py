from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Serializers
from user.serializers import UserLoginSerializer, UserModelSerializer, UserRegisterSerializer

# Models
from user.models import User

JWT_Authenticator = JWTAuthentication()

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)
