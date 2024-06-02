from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    dob = models.DateField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} has been created with next email: {self.email}"

    class Meta:
        db_table = "users"


class Instructor(User):
    instructor_id = models.BigAutoField(primary_key=True)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return f"First name: {self.firstname}; \nLast name: {self.lastname}; \nIs full time: {self.full_time}; \nTotal learners: {self.total_learners}"

    class Meta:
        db_table = "instructors"


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

    learner_id = models.BigAutoField(primary_key=True)
    occupation = models.CharField(
        null=False, max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nDob: {self.dob}\nOccupation: {self.occupation}\nSocial link: {self.social_link}"

    class Meta:
        db_table = "learners"


class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100, default="online course")
    description = models.CharField(null=False, max_length=500)

    # Many-to-many relationship with Learner via Enrollment
    learners = models.ManyToManyField(Learner, through="Enrollment")

    # Many-to-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return f"Course name: {self.name}; Description: {self.description};"

    class Meta:
        db_table = "courses"

class Lesson(models.Model):
    lesson_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Lesson title: {self.title}; Course: {self.course};"

    class Meta:
        db_table = "lessons"


# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = "audit"
    HONOR = "honor"

    COURSE_MODES = [
        (AUDIT, "Audit"),
        (HONOR, "Honor"),
    ]

    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=timezone.now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

    def __str__(self):
        return f"Learner: {self.learner}; Course: {self.course}; Mode: {self.mode};"

    class Meta:
        db_table = "enrollments"
