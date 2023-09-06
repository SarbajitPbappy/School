from django.contrib import admin
from .models import Department, Course
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('department_name',)}
    list_display = ('department_name', 'slug')
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title','course_price', 'course_department','created_date', )
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)