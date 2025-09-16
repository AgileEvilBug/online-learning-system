from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Enrollment

@login_required
def enroll_in_course(request, slug):
    course = get_object_or_404(Course, slug=slug, published=True)
    if not request.user.is_student:
        return redirect(course.get_absolute_url())
    Enrollment.objects.get_or_create(student=request.user.student, course=course)
    return redirect('student-dashboard')
