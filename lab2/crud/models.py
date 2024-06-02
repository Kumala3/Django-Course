from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} has been created with next email: {self.email}"


class Instructor(User):
    position = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.username} is an {self.position} in the {self.department} department"
