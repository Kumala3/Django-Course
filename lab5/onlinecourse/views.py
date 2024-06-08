from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.views import View


class TopCoursesList(View):
    def get(self, request):
        context = {}
        courses = Course.objects.order_by("-total_enrollment")[:10]
        context["course_list"] = courses
        return render(request, "onlinecourse/course_list.html", context)
