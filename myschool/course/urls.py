from django.urls import path
from . import views


urlpatterns = [
    path('course_list/', views.course_list, name='course_list'),
    path('course_list/<slug:department_slug>/', views.course_list, name='course_by_dep'),
    path('update_course/<int:pk>/', views.CourseUpdateFormView.as_view(), name='update_course'),
    path('delete_course/<int:pk>/', views.DeleteCourseFormView.as_view(), name='delete_course'),
    path('add_course/', views.AddCourseFormView.as_view(), name='add_courses'),
    path('search/', views.search, name='search'),
]