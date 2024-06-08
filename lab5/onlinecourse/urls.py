from django.urls import path
from .views import TopCoursesList

app_name = "onlinecourse"

urlpatterns = (
    [
        path("top-courses/", TopCoursesList.as_view(), name="popular_course_list")
    ]
)
