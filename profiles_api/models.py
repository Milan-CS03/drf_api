from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """user profile manager"""

    def create_user(self, email, name, password=None):
        """New user creation"""
        if not email:
            raise ValueError("please provide email address")
        email = self.normalize_email(email)
        user = self.model(email, name)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """create superuser"""
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DB model for system users"""
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full username"""
        return self.name

    def get_short_name(self):
        """retrieve short name"""
        return self.name

    def __str__(self):
        """string rep of class """
        return self.email
