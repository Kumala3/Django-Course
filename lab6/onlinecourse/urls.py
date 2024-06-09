from django.urls import path
from .views import CourseListView, CourseDetailsView, EnrollView

app_name = "onlinecourse"
urlpatterns = [
    path("", CourseListView.as_view(), name="popular_course_list"),
    path("course-details/", CourseDetailsView.as_view(), name="course_details"),
    path("course/<int:pk>/enroll/", EnrollView.as_view(), "enroll"),
]
