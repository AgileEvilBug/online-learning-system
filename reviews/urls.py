from django.urls import path
from .views import review_create

urlpatterns = [
    path('create/', review_create, name='review-create'),
]
