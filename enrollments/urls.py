from django.urls import path
from .views import enroll_in_course

urlpatterns = [
    path('<slug:slug>/enroll/', enroll_in_course, name='enroll-course'),
]
