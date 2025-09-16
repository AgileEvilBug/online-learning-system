from django.contrib import admin
from .models import Category, Tag, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category', 'price', 'published')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('published', 'category', 'tags')

admin.site.register(Category)
admin.site.register(Tag)
