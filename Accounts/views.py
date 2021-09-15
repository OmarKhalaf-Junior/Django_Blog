from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import CreateProfileForm, UpdateProfileForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username= username, password= password)
            login(request, user)
            return redirect('/')
    else:
        form= UserCreationForm()

    return render(request, 'registration/signup.html', {'form':form})

def show_profile(request, pk):
    profile= get_object_or_404(Profile, pk= pk)
    return render(request, 'registration/show_profile.html', {'profile': profile})


def create_profile(request):
    if request.method == 'POST':
        form= CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            myform= form.save(commit= False)
            myform.user= request.user
            myform.save()
            return redirect('/')

    else:
        form= CreateProfileForm()

    return render(request, 'registration/create_profile.html', {'form': form})


def update_profile(request, pk):
    profile= get_object_or_404(Profile, pk= pk)
    if request.method == 'POST':
        form= UpdateProfileForm(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()

    else:
        form= UpdateProfileForm(instance= profile)
    return render(request, 'registration/update_profile.html', {'form': form})
