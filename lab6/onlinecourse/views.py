from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404, HttpRequest

class CourseListView(View):
    def get(self, request: HttpRequest):
        context = {}
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)


class CourseDetailsView(View):
    def get(self, request: HttpRequest):
        context = {}
        course_id = request.GET.get('course_id')
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            return render(request, 'onlinecourse/course_detail.html', context)
        except Course.DoesNotExist:
            raise Http404("No course matches the given id.")


class EnrollView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        course_id = kwargs.get("pk")
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse('onlinecourse:course_details'), args=(course_id))
