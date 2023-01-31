from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
now = timezone.now()

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """User model used for authentication and microblog authoring."""

    username = None
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class BankModel(models.Model):
    taken = models.BooleanField(default=False, blank=False)
    ids = models.PositiveIntegerField(default=0, blank=False)
    assets = models.PositiveIntegerField(default=0, blank=False)
    name = models.CharField(max_length=100, blank=False)
    fullName = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(User,default=now, on_delete = models.CASCADE, related_name = 'owner')
    b75 = models.FloatField(default=0, blank=False)
    b76 = models.FloatField(default=0, blank=False)
    b77 = models.FloatField(default=0, blank=False)
    b78 = models.FloatField(default=0, blank=False)
    b111 = models.FloatField(default=0, blank=False)
    c89 = models.FloatField(default=0, blank=False)
    c84 = models.FloatField(default=0, blank=False)
    c85 = models.FloatField(default=0, blank=False)
    b108 = models.FloatField(default=0, blank=False)
    year = models.IntegerField(default=0, blank=False)

class YearModel(models.Model):
    bank = models.ForeignKey(BankModel,default=now, on_delete = models.CASCADE, related_name = 'bank')
    d75 = models.FloatField(default=0, blank=False)
    d76 = models.FloatField(default=0, blank=False)
    d77 = models.FloatField(default=0, blank=False)
    d78 = models.FloatField(default=0, blank=False)
    d111 = models.FloatField(default=0, blank=False)
    e89 = models.FloatField(default=0, blank=False)
    e84 = models.FloatField(default=0, blank=False)
    e85 = models.FloatField(default=0, blank=False)
    d108 = models.FloatField(default=0, blank=False)
    year = models.IntegerField(default=0, blank=False)
