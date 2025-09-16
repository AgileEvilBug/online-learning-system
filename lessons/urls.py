from django.urls import path
from .views import lesson_create

urlpatterns = [
    path('create/', lesson_create, name='lesson-create'),
]
