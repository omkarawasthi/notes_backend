import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField(unique=True)
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    username = None
    email = None
    first_name = None
    last_name = None
    
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.user_email
