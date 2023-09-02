from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView  # Import ListView
from .models import Course
from .forms import CourseForm

@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CourseListView(ListView):  # Create a ListView for course listing
    model = Course
    template_name = 'course/course_list.html'  # Use the template you've created
    context_object_name = 'courses'  # Specify the context variable name
