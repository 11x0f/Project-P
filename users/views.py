from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer, CustomTokenSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def patch(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(
            profile,
            data = request.data,
            partial = True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response (serializer.erros, status  = status.HTTP_400_BAD_REQUEST)
