from django.urls import path
from .views import role_redirect, student_dashboard, instructor_dashboard, employee_dashboard

urlpatterns = [
    path('role-redirect/', role_redirect, name='role-redirect'),
    path('student/', student_dashboard, name='student-dashboard'),
    path('instructor/', instructor_dashboard, name='instructor-dashboard'),
    path('employee/', employee_dashboard, name='employee-dashboard'),
]
