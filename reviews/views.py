from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ReviewForm

def is_student(user): return getattr(user, 'is_student', False)

@login_required
@user_passes_test(is_student)
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user.student
            review.save()
            return redirect(review.course.get_absolute_url())
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})
