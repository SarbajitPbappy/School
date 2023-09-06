from django.shortcuts import render, redirect
from .models import Course, Department
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import CourseForm
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from MySchool import urls as home_urls
# Create your views here.


def course_list(request, department_slug=None):
    course_list = None
    department_list = Department.objects.all()
    if department_slug:
        department = get_object_or_404(Department, slug=department_slug)
        course_list = Course.objects.filter(course_department=department)
    else:
        course_list = Course.objects.all()

    context = {'course_list': course_list,
               'department_list': department_list, }
    return render(request, 'course/course_list.html', context)


class AddCourseFormView(CreateView):
    model = Course
    template_name = 'course/add_courses.html'
    form_class = CourseForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.course_teacher = self.request.user
        form.save()
        return super().form_valid(form)


class DeleteCourseFormView(DeleteView):
    model = Course
    template_name = 'course/delete.html'
    success_url = reverse_lazy('dashboard')


class CourseUpdateFormView(UpdateView):
    model = Course
    template_name = 'course/add_courses.html'
    form_class = CourseForm
    success_url = reverse_lazy('dashboard')


def search(request):
    course_list = None
    if request.method == 'POST':
        searched = request.POST['searched']
        course_list = Course.objects.order_by('-created_date').filter(
            Q(course_description__icontains=searched) | Q(course_title__icontains=searched))
        return render(request, 'course/search.html', {'course_list': course_list})
    else:
        return render(request, 'course/search.html', {'course_list': course_list})
