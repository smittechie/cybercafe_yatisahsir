from django.db import models
from django.contrib.auth.models import AbstractUser
from . import choices
from .choices import Choice_2070, INTEL, MB, AVAILABLE, RAM_16


# Create your models here.

class User(AbstractUser):
    mobile_number = models.IntegerField()
    email = models.EmailField(unique=True)
    id_proof = models.IntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile_number', 'id_proof']

    def __str__(self):
        return self.username


class System(models.Model):
    name = models.CharField(max_length=24)
    graphic_card = models.CharField(max_length=20, choices=choices.GRAPHIC, default=Choice_2070)
    processor = models.CharField(max_length=20, choices=choices.PROCESSOR, default=INTEL)
    ram = models.IntegerField(choices=choices.RAM, default=RAM_16)
    ram_unit = models.CharField(max_length=20, choices=choices.RAM_UNIT, default=MB)
    status = models.CharField(max_length=20, choices=choices.STATUS, default=AVAILABLE)

    def __str__(self):
        return self.name


class Status(models.Model):
    user_system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="user_system")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_status')


class History(models.Model):
    # user_history = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_history")
    # user_system_history = models.ForeignKey(System, on_delete=models.CASCADE, related_name="user_system_history")
    user_system_history = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="user_system_history")
    login_time = models.TimeField()
    logout_time = models.TimeField()
