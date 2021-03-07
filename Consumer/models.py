from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from decouple import config
import json
from django.contrib.auth import authenticate, get_user_model
import uuid
from django.db import models

# https://github.com/Tivix/django-rest-auth/issues/464
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """Create and save a regular User with the given username and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """Create and save a SuperUser with the given username and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("username (deprecated)"),  unique=True, blank=True, max_length=255)

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse("username:detail", kwargs={"email": self.email})

    def token(self):

        refreshToken = RefreshToken.for_user(self)
        accessToken = refreshToken.access_token
        
        decodeJTW = jwt.decode(str(accessToken), config('SECRET_KEY'), algorithms=["HS256"]);

        permisions = []
        for  p in list(self.get_group_permissions()):
            permisions.append(p.replace('.',' | '))

        groups =  list(self.groups.values_list('name',flat = True)) # QuerySet Object

        # for JTW payload
        decodeJTW['PERMISIONS'] = permisions
        # decodeJTW['groups'] = groups
        decodeJTW['USERNAME'] = self.username
        decodeJTW['ID_CONSUMER'] = str(self.id)
        decodeJTW['EXP'] = decodeJTW['exp']

        #encode
        encoded = jwt.encode(decodeJTW, config('SECRET_KEY'), algorithm="HS256")

        return ({
            'refresh': str(refreshToken),
            'access': encoded,
        })