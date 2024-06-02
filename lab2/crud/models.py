from django.db import models
from django.utils import timezone


class User(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=100, null=False)
    dob = models.DateField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} has been created with next email: {self.email}"


class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return f"First name: {self.firstname}; \nLast name: {self.lastname}; \nIs full time: {self.full_time}; \nTotal learners: {self.total_learners}"


class Learner(User):
    STUDENT = "student"
    DEVELOPER = "developer"
    DATA_SCIENTIST = "data_scientist"
    DATABASE_ADMIN = "dba"

    OCCUPATION_CHOICES = [
        (STUDENT, "Student"),
        (DEVELOPER, "Developer"),
        (DATA_SCIENTIST, "Data Scientist"),
        (DATABASE_ADMIN, "Database Admin"),
    ]

    occupation = models.CharField(
        null=False, max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nDob: {self.dob}\nOccupation: {self.occupation}\nSocial link: {self.social_link}"


class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default="online course")
    description = models.CharField(null=False, max_length=500)

    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return f"Course name: {self.name}; Description: {self.description};"


class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    content = models.TextField()

    def __str__(self):
        return f"Lesson title: {self.title}; Course: {self.course};"
