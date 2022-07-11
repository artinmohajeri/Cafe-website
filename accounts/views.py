from django.shortcuts import render
from .forms import AddExperienceForm
from .models import AddExperience
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
# from .models import Post, Comment, Sample
from django.urls import reverse
# Create your views here.


def register(request):
    return render(request, 'accounts/register.html', {})


def profile(request):
    return render(request, 'accounts/profile.html', {})


def add_exp(request):
    if request.method == "POST":
        form = AddExperienceForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddExperienceForm()

    return render(request,
              'accounts/add-exp.html',
              {
                'form':form
              })


def create_profile(request):
    return render(request, 'accounts/create-profile.html', {})


def login_func(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(to=reverse('create_profile'))
        else:
            messages.add_message(request,messages.ERROR,"username or password is not correct")
    return render(request,'accounts/login.html',{})
