from django.shortcuts import render ,redirect
from .models import *
from .forms import ProfileForm, ProjectForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'Login.html')

def signup(request):
    return render(request, 'Signup.html')

def home(request):
    profile = Profile.objects.all()
    projects = ProjectBoard.objects.all()
    context = {'profile' : profile, 'projects': projects}
    return render(request, 'Home.html', context)

# def edit(request):
#     return render(request, 'Edit.html')

def edit(request):
    if request.method=='POST':
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProfileForm()
    return render(request, 'Edit.html', {'form': form})

def project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProjectForm()
    return render(request, 'Project.html', {'form': form})