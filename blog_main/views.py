from django.shortcuts import render, redirect

from blogs.models import Category, Blog
from assignments.models import About, SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by("updated_at")
    recent_posts = Blog.objects.filter(is_featured=False, status="Published").order_by("-created_at")
    socials=SocialLink.objects.filter()
    
    # fetch about us
    try:
        about =About.objects.get()
    
    except:
        about=None
        

        
    context = {
        "featured_posts":featured_posts,
        "recent_posts":recent_posts,
        'about':about,
        'socials':socials,
    }
    return render(request, "home.html", context)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    
    context={
        'form':form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        return redirect('home')
    form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
