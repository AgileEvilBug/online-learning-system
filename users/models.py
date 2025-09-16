from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    STUDENT = 'student'
    INSTRUCTOR = 'instructor'
    EMPLOYEE = 'employee'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (INSTRUCTOR, 'Instructor'),
        (EMPLOYEE, 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # handy flags
    @property
    def is_student(self): return self.role == self.STUDENT
    @property
    def is_instructor(self): return self.role == self.INSTRUCTOR
    @property
    def is_employee(self): return self.role == self.EMPLOYEE

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    def __str__(self): return f"Student: {self.user.username}"

class Instructor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    def __str__(self): return f"Instructor: {self.user.username}"

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    def __str__(self): return f"Employee: {self.user.username}"
