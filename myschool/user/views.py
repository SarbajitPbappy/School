# user/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('course_list') 
        else:
            error_message = 'Invalid login credentials'
    else:
        error_message = None

    return render(request, 'user/login.html', {'error_message': error_message})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')
