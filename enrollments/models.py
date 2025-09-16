from django.db import models
from django.conf import settings

class Enrollment(models.Model):
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='enrollments')
    started_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_lessons = models.ManyToManyField('lessons.Lesson', blank=True)

    class Meta:
        unique_together = ('student', 'course')

    def progress_percent(self):
        total = self.course.lessons.count()
        if total == 0: return 0
        done = self.completed_lessons.count()
        return int(done * 100 / total)

    def __str__(self): return f"{self.student} -> {self.course}"
