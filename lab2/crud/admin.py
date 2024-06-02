from django.contrib import admin

from .models import User, Course, Instructor, Learner, Enrollment, Lesson


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "dob", "created_at"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "dob", "full_time", "total_learners"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["course", "content", "title"]


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "dob", "social_link", "occupation"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["date_enrolled", "course", "learner", "mode"]
