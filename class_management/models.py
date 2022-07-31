import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class School(models.Model):
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.school_name}"


class Classroom(models.Model):
    title = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.title}"


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    class_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.full_name}"
