from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpRequest
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth import login, logout, authenticate
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create authentication related views
class LogoutView(View):
    def get(self, request: HttpRequest):
        print(f"Log out the user: {request.user.username}")

        logout(request)
        return redirect("onlinecourse:popular_course_list")


class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, "onlinecourse/user_login.html")

    def post(self, request: HttpRequest):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("onlinecourse:popular_course_list")
        else:
            return render(
                request, "onlinecourse/user_login.html", {"error": "Invalid login"}
            )


class RegistrationView(View):
    def get(self, request: HttpRequest):
        return render(request, "onlinecourse/user_registration.html")

    def post(self, request: HttpRequest):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("onlinecourse:popular_course_list")


# Add a class-based course list view
class CourseListView(generic.ListView):
    template_name = "onlinecourse/course_list.html"
    context_object_name = "course_list"

    def get_queryset(self):
        courses = Course.objects.order_by("-total_enrollment")[:10]
        return courses


# Add a generic course details view
class CourseDetailsView(generic.DetailView):
    model = Course
    template_name = "onlinecourse/course_detail.html"


class EnrollView(View):
    # Handles get request
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get("pk")
        course = get_object_or_404(Course, pk=course_id)
        # Create an enrollment
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(
            reverse(viewname="onlinecourse:course_details", args=(course.id,))
        )
