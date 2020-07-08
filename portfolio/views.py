from django.shortcuts import render, get_object_or_404
from .models import Project, User

def login(request):
    session = request.session
    if session.__contains__('logged') and session.get('logged'):
        projects = Project.objects.all()
        return render(request, 'portfolio/home.html', {'projects': projects})
    else:
        return render(request, 'portfolio/login.html')

def logout(request):
    session = request.session
    if 'logged' in session.keys():
        session.__delitem__('logged')

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
    projects = Project.objects.all()
    user = None
    try:
        num_of_visits  = request.session.get('visits', 0)
        is_user_logged = request.session.get('logged', False)
        if not is_user_logged:
            email = request.GET.get('email')
            password = request.GET.get('password')
            user = User.objects.get(email=email, password=password)
            request.session['name']   = f'{user.first_name} {user.last_name}'
            request.session['logged'] = True
            request.session['visits'] = num_of_visits + 1
        return render(request, 'portfolio/home.html', {'projects': projects})
    except User.DoesNotExist:
        return render(request, 'portfolio/login.html', {'message': 'Incorrect user/password.'})
    

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'portfolio/project.html', {'project': project})

