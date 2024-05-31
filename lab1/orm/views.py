from django.http import HttpResponse


def home():
    return HttpResponse("Welcome to first Django app within this course!")
