from .serializers import RegisterUserSerializer
from rest_framework.response import Response
from ...models import CustomUser
from rest_framework.generics import CreateAPIView
from rest_framework import status
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterUserGeneric(CreateAPIView):
    # create user with send token to email
    queryset=User.objects.all()
    serializer_class=RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
