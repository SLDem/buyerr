from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class UserManager(BaseUserManager):

    def _create_user(self, name, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, password, **extra_fields):
        return self._create_user(name, email, password, False, False, **extra_fields)

    def create_superuser(self, name, email, password, **extra_fields):
        user = self._create_user(name, email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects: models.Manager()
    objects = UserManager()

    email = models.EmailField('Email', max_length=254, unique=True)
    name = models.CharField('Full Name', max_length=35, unique=True, null=False, blank=False)

    phone = models.CharField('Phone', max_length=12, unique=True, null=True, blank=True)
    gender = models.BooleanField(default=True)
    birthday = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=0)

    delivery_address = models.CharField('Delivery Address', max_length=500, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name

