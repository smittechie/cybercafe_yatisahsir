from django.db import models
from django.contrib.auth.models import AbstractUser
from . import choices


# Create your models here.

class User(AbstractUser):
    mobile_number = models.IntegerField()
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile_number']

    def __str__(self):
        return self.username


class System(models.Model):
    name = models.CharField(max_length=24)
    company = models.CharField(max_length=25)
    ram_GB = models.IntegerField()
    display = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Status(models.Model):
    user_system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="user_system")
    system_status = models.CharField(
        max_length=20,
        choices=choices.STATUS,
        default='Available'
    )


class History(models.Model):
    user_history = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_history")
    user_system_history = models.ForeignKey(System, on_delete=models.CASCADE, related_name="user_system_history")
    login_time = models.TimeField()
    logout_time = models.TimeField()
