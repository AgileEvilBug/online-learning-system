from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    def save(self, *a, **kw):
        if not self.slug: self.slug = slugify(self.name)
        return super().save(*a, **kw)
    def __str__(self): return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    def save(self, *a, **kw):
        if not self.slug: self.slug = slugify(self.name)
        return super().save(*a, **kw)
    def __str__(self): return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    instructor = models.ForeignKey('users.Instructor', on_delete=models.CASCADE, related_name='courses')
    tags = models.ManyToManyField(Tag, blank=True, related_name='courses')

    class Meta:
        ordering = ['-created_at']

    def save(self, *a, **kw):
        if not self.slug: self.slug = slugify(self.title)
        return super().save(*a, **kw)

    def __str__(self): return self.title
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('course-detail', args=[self.slug])
