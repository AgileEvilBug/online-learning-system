from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('create/', views.course_create, name='course-create'),
    path('<slug:slug>/', views.course_detail, name='course-detail'),
    path('<slug:slug>/edit/', views.course_update, name='course-update'),
]
