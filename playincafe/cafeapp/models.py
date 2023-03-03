from django.db import models
from django.contrib.auth.models import AbstractUser
from . import choices
from .choices import Choice_2070, INTEL, MB, AVAILABLE, RAM_16
from django.utils import timezone

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_system', null=True, blank=True)

    def __str__(self):
        return self.name


class History(models.Model):
    user_history = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_history")
    system_name = models.ForeignKey(System, on_delete=models.CASCADE, related_name="system_name")
    login_time = models.DateTimeField(default=timezone.now())
    logout_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default= False)

    def soft_deleted(self):
        self.is_deleted= True
        self.save()