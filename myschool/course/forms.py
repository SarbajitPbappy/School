from django.forms import ModelForm
from .models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_title', 'course_description','course_banner', 'course_price', 'course_department']
        labels = {
            'course_title' : 'Title',
            'course_description' : 'Description',
            'course_price': 'Price',
            'course_department' : 'Department',
            'course_banner': 'Banner',
        }