from django.shortcuts import render, get_object_or_404
from .models import Project, User

def login(request):
    return render(request, 'portfolio/login.html')

def signup(request):
    return render(request, 'portfolio/signup.html')

def welcome(request):
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    email = request.GET.get('email')
    password = str(request.GET.get('password1'))
    password_2 = str(request.GET.get('password2'))

    if password == password_2:
        user = User(first_name=fname, last_name=lname, email=email, password=password)
        user.save()
        return render(request, 'portfolio/welcome.html', {'user': user})
    else:
        return render(request, 'portfolio/signup.html')
    

def home(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    projects = Project.objects.all()
    user = None
    try:
        user = User.objects.get(email=email, password=password)
        return render(request, 'portfolio/home.html', {'projects': projects, 'user': user})
    except User.DoesNotExist:
        return render(request, 'portfolio/login.html', {'message': 'Incorrect user/password.'})
    

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})

