from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.views import View


class TopCoursesList(View):
    def get(self, request: HttpRequest):
        context = {}
        courses = Course.objects.order_by("-total_enrollment")[:10]
        context["course_list"] = courses
        return render(request, "onlinecourse/course_list.html", context)


class EnrollCourse(View):
    def post(self, request: HttpRequest, course_id: int):
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(
            reverse(viewname="onlinecourse:course_details", args=(course_id,))
        )


class CourseDetails(View):
    def get(self, request: HttpRequest, course_id: int):
        try:
            course = Course.objects.get(pk=course_id)
            context = {"course": course}
            return render(request, "onlinecourse/course_detail.html", context)
        except Course.DoesNotExist:
            raise Http404("Course does not exist")
