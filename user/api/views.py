from user.models import User 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializers import RegisterUserSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    permission_classes = [IsAuthenticated]

    def get (self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        userId = request.user.id
        user = User.objects.get(id=userId)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

