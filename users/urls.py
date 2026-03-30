from django.urls import path
from .views import RegisterView
from .views import CustomTokenView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
]