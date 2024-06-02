# Django specific settings
import os
from crud.models import User, Learner, Course, Enrollment, Instructor, Lesson
from datetime import date
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()


def write_instructors():
    # Add instructors
    # Create a user
    user_john = User(first_name="John", last_name="Doe", dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()

    instructor_yan = Instructor(
        first_name="Yan",
        last_name="Luo",
        dob=date(1962, 7, 16),
        full_time=True,
        total_learners=30050,
    )
    instructor_yan.save()

    instructor_joy = Instructor(
        first_name="Joy",
        last_name="Li",
        dob=date(1992, 1, 2),
        full_time=False,
        total_learners=10040,
    )
    instructor_joy.save()

    instructor_peter = Instructor(
        first_name="Peter",
        last_name="Chen",
        dob=date(1982, 5, 2),
        full_time=True,
        total_learners=2002,
    )
    instructor_peter.save()
    print("Instructor objects all saved... ")


def write_courses():
    # Add Courses
    course_cloud_app = Course(
        name="Cloud Application Development with Database",
        description="Develop and deploy application on cloud",
    )

    course_cloud_app.save()
    course_python = Course(
        name="Introduction to Python",
        description="Learn core concepts of Python and obtain hands-on "
        "experience via a capstone project",
    )
    course_python.save()

    print("Course objects all saved... ")


def write_lessons():
    # Add lessons
    lesson_1 = Lesson(title="Lesson 1", content="Object-relational mapping project")
    lesson_1.save()

    lesson_2 = Lesson(title="Lesson 2", content="Django full stack project")
    lesson_2.save()

    print("Lesson objects all saved... ")


