from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import User, Student, Instructor, Employee

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance: User, created, **kwargs):
    if not created:
        return
    if instance.role == User.STUDENT:
        Student.objects.get_or_create(user=instance)
    elif instance.role == User.INSTRUCTOR:
        Instructor.objects.get_or_create(user=instance)
    elif instance.role == User.EMPLOYEE:
        Employee.objects.get_or_create(user=instance)
