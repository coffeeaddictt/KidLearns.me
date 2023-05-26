from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.

def home(request):
    return render(request,'accounts/index.html')

def about(request):
    return render(request,'accounts/about.html')

def contact(request):
    return render(request,'accounts/contact.html')

def courses(request):
    return render(request,'accounts/courses.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request,'accounts/login.html', context)

def registerpage(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', { 'form': form})   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
        
    return render(request,'accounts/register.html')


