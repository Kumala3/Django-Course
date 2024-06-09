from django.urls import path
from .views import TopCoursesList, EnrollCourse, CourseDetails

app_name = "onlinecourse"

urlpatterns = (
    [
        path("top-courses/", TopCoursesList.as_view(), name="popular_course_list"),
        path("course/<int:course_id>/enroll/", EnrollCourse.as_view(), name="enroll"),
        path("course/<int:course_id>/", CourseDetails.as_view(), name="course_details"),
    ]
)
