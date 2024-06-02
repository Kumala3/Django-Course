from django.contrib import admin

from .models import User, Course, Instructor, Learner, Enrollment, Lesson


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["__all__"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["__all__"]


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["__all__"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["__all__"]


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ["__all__"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["__all__"]
