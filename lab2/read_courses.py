# Django specific settings
import os

from crud.models import Course

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

try:
    from crud.models import Course
except ImportError:
    print("Unable to import models from crud.models. Please check the path to the models.")

# Your code starts from here:
courses = Course.objects.all()

for course in courses:
    print(course)
