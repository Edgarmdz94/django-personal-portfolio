from django.shortcuts import render, get_object_or_404
from .models import Project, Login

def login(request):
    return render(request, 'portfolio/login.html')

def home(request):
    email = request.GET.get('email')
    password = request.GET.get('password')

    user = Login.objects.get(email=email, password=password)

    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'user': user})

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})

