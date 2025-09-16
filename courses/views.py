from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Course, Category, Tag
from .forms import CourseForm

def course_list(request):
    qs = Course.objects.filter(published=True)
    q = request.GET.get('q')
    cat = request.GET.get('category')
    tag = request.GET.get('tag')
    if q:
        qs = qs.filter(title__icontains=q)
    if cat:
        qs = qs.filter(category__slug=cat)
    if tag:
        qs = qs.filter(tags__slug=tag)
    return render(request, 'courses/course_list.html', {
        'courses': qs.select_related('instructor__user', 'category').prefetch_related('tags'),
        'categories': Category.get_queryset().all() if hasattr(Category, 'get_queryset') else Category.objects.all(),
        'tags': Tag.objects.all()
    })

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, published=True)
    return render(request, 'courses/course_detail.html', {'course': course})

def is_instructor(user):
    return getattr(user, 'is_instructor', False)

@login_required
@user_passes_test(is_instructor)
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user.instructor  # from profile
            course.save()
            form.save_m2m()
            return redirect(course.get_absolute_url())
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

@login_required
@user_passes_test(is_instructor)
def course_update(request, slug):
    course = get_object_or_404(Course, slug=slug, instructor=request.user.instructor)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect(course.get_absolute_url())
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})
