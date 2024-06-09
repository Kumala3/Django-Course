from django.urls import path
from . import views

app_name = "onlinecourse"
urlpatterns = [
    path(
        route="course/<int:pk>/enroll/", view=views.EnrollView.as_view(), name="enroll"
    ),
    path(route="", view=views.CourseListView.as_view(), name="popular_course_list"),
    path(
        route="course/<int:pk>/",
        view=views.CourseDetailsView.as_view(),
        name="course_details",
    ),
    path("logout/", view=views.LogoutView.as_view(), name="logout"),
    path("login/", view=views.LoginView.as_view(), name="login"),
    path("registration/", view=views.RegistrationView.as_view(), name="registration"),
]
