import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


class SuperUser(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True")
        return self.create_user(email, password, **extra_fields)


def user_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{extension}"
    return f"profiles/{timezone.now().date().strftime('%Y/%m/%d')}/{filename}"

# def user_directory_path(instance, filename):
#     extension = filename.split('.')[-1]
#     filename = f"{instance.unique_id}.{extension}"
#     return f"profiles/user_{instance.owner.unique_id}/{timezone.now().date().strftime('%Y/%m/%d')}/{filename}"
#
#
# class UserImage(models.Model):
#     owner = models.ForeignKey('User', on_delete=models.CASCADE)
#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     image = models.ImageField(upload_to=user_directory_path, default='default.jpg', blank=True, null=True,
#                               verbose_name="Аватар")
#
#     def __str__(self):
#         return f"{self.image}"
#
#     class Meta:
#         verbose_name = "Изображение пользователя"
#         verbose_name_plural = "Изображения пользователей"


class User(AbstractBaseUser, PermissionsMixin):
    TYPE_ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
    ]
    email = models.EmailField(unique=True, verbose_name="Почта")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=13, blank=True, verbose_name="Номер телефона")
    # unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # image = models.ForeignKey(UserImage, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Аватар")
    image = models.ImageField(upload_to=user_directory_path, default='default.jpg', blank=True, verbose_name="Аватар")
    user_type = models.CharField(max_length=255, choices=TYPE_ROLE_CHOICES, verbose_name="Тип пользователя")
    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_superuser = models.BooleanField(default=False, verbose_name="Суперь пользователь")

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = SuperUser()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Системный пользователь'
        verbose_name_plural = "Системные пользователи"
