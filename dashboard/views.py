from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from courses.models import Course
from enrollments.models import Enrollment


@login_required
def role_redirect(request):
    u = request.user
    if u.is_employee:
        return redirect('employee-dashboard')
    if u.is_instructor:
        return redirect('instructor-dashboard')
    return redirect('student-dashboard')


@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return redirect('role-redirect')
    enrolls = (Enrollment.objects
               .filter(student=request.user.student)
               .select_related('course__instructor__user')
               .prefetch_related('course__lessons'))
    return render(request, 'dashboard/student.html', {'enrollments': enrolls})


@login_required
def instructor_dashboard(request):
    if not request.user.is_instructor:
        return redirect('role-redirect')
    my_courses = (Course.objects
                  .filter(instructor=request.user.instructor)
                  .prefetch_related('lessons', 'enrollments'))
    return render(request, 'dashboard/instructor.html', {'courses': my_courses})


@login_required
def employee_dashboard(request):
    if not request.user.is_employee:
        return redirect('role-redirect')
    counts = {
        'courses': Course.objects.count(),
        'enrollments': Enrollment.objects.count(),
    }
    return render(request, 'dashboard/employee.html', {'counts': counts})
