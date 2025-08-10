from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, user_email, user_name, password, **extra_fields):
        """
        Create and save a User with the given email, username, and password.
        """
        if not user_email:
            raise ValueError('The Email must be set')
        if not user_name:
            raise ValueError('The User Name must be set')
        
        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        # We call our custom create_user method
        return self.create_user(user_email, user_name, password, **extra_fields)