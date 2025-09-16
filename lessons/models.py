from django.db import models

class Lesson(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)
    video_url = models.URLField(blank=True)  # or store video file if you want
    resource = models.FileField(upload_to='lesson_resources/', blank=True, null=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['order']
        unique_together = ('course', 'order')

    def __str__(self):
        return f"{self.course.title} - {self.order}. {self.title}"
