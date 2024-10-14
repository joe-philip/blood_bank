from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from .choices import GenderChoices

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    initials = models.JSONField(default=list)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    blood_group = models.ForeignKey(
        'admin_user.BloodGroups',
        related_name='users',
        on_delete=models.DO_NOTHING
    )
    role = models.ForeignKey(
        'admin_user.Roles',
        related_name='users',
        on_delete=models.DO_NOTHING
    )
    dob = models.EmailField(null=True)
    last_donated = models.DateTimeField(null=True)
    is_available_for_donation = models.BooleanField(default=False)
    gender = models.CharField(choices=GenderChoices.choices)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'blood_group', 'role', 'gender')

    objects = BaseUserManager()

    def __str__(self) -> str: return self.email
