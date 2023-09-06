from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    
    def __str__(self):
        return self.department_name
    
class Course(models.Model):
    course_title = models.CharField(max_length=100, unique=True)
    course_description = models.TextField(max_length=400)
    course_teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course_banner = models.ImageField(upload_to='photos/courses', blank=True)
    course_price = models.IntegerField()
    course_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    