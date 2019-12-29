from django.db import models

# Create your models here.
# implementing custom user model here: 20191228
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):
    # custom class with helper methods for creating and managing users and superusers
    def create_user(self, email, password=None, **extra_fields):
        # creates and saves a new user
        # inherits from djangos BaseUserManager
        # anything additional will be agglomerated into extra_fields
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # our custom user model that supports using email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
