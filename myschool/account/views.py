from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from course.models import Course

from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'GET':
        return render(request, 'accounts/register.html', {'form':form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name)
        
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    course_list = None
    if request.user is not None:
        course_list = Course.objects.filter(course_teacher=request.user)
    return render(request, 'accounts/dashboard.html', {'course_list': course_list})