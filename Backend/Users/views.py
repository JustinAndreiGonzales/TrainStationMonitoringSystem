from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db import connection, OperationalError
from rest_framework import status

from .serializers import UserSerializer

# Create your views here.
User = get_user_model()

class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def check_database_status(self):
        try:
            connection.ensure_connection()
            return True
        except OperationalError:
            return False

    def post(self, request, *args, **kwargs):
        if not self.check_database_status():
            return Response(
                {"error": "Database connection error"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response({
                    "message": "User created successfully",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "role": user.role
                    }
                }, status=201) 
            except OperationalError:
              return Response(
                {"error": "Database connection error"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        data['username'] = self.user.username

        return data
    
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def check_database_status(self):
        try:
            connection.ensure_connection()
            return True
        except OperationalError:
            return False

    def post(self, request, *args, **kwargs):
        if not self.check_database_status():
            return Response(
                {"error": "Database connection error"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        return super().post(request, *args, **kwargs)


# secured views
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "You are authenticated!"})