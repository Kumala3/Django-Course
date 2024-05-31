from django.db import models

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=8)
    residence = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} has successfully created. Users's id: {self.user_id}"
