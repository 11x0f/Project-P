from django.db import models
import uuid 
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.choices import LevelChoices

class User(AbstractUser):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)

    user = models.OneToOneField(
        User, 
        on_delete = models.CASCADE,
        related_name = 'profile'
    )

    full_name = models.CharField(max_length =255, blank = True)
    bio = models.TextField(blank = True)
    profile_image_user = models.TextField(blank=True)

    level = models.CharField(
        max_length = 20,
        choices = LevelChoices.choices,
        null = True,
        blank = True
    )

    assessment_completed = models.BooleanField(default=False)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.email} Profile"
