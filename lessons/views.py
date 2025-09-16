from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LessonForm

def is_instructor(user): return getattr(user, 'is_instructor', False)

@login_required
@user_passes_test(is_instructor)
def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save()
            return redirect(lesson.course.get_absolute_url())
    else:
        form = LessonForm()
    return render(request, 'lessons/lesson_form.html', {'form': form})
