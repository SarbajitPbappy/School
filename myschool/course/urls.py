from django.urls import path
from .views import CourseCreateView, CourseListView  # Import CourseListView

urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='create_course'),
    path('list/', CourseListView.as_view(), name='course_list'),  
]
