from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})

