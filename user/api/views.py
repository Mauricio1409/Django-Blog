from user.models import User 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializers import RegisterUserSerializer

class RegisterView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = RegisterUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

