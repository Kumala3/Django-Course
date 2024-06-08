from django.contrib import admin
from .models import Course, Instructor, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "total_enrollment", "description", "pub_date")


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("full_time", "total_learners")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "course")
