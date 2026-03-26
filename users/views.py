from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer, CustomTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer