from django.shortcuts import render
from course.models import Course,Department
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    course_list = Course.objects.all()
    context = {'course_list':course_list}
    return render(request, 'index.html', context)