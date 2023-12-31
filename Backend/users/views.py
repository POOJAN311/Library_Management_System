from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializer import UserCreateSerailizer,UserSerailizer

class RegisterView(APIView):
    def post(self, request):
        data = request.data

        serializer = UserCreateSerailizer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.create(serializer.validated_data)
        user = UserSerailizer(user)
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user =  request.user
        user = UserSerailizer(user)
        

        return Response(user.data, status=status.HTTP_200_OK)