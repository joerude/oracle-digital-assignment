from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    username = None
    mobile_number = models.CharField(max_length=15, unique=True)
    class_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    USERNAME_FIELD = 'mobile_number'
