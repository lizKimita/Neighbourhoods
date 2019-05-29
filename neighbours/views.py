from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import NewPostForm, NewBusinessForm, NewProfileForm
from .models import Profile, Businesses, Posts

# Create your views here.

def home(request):
    current_user = request.user
    posts = Posts.get_posts()
    title = "Neighborhoods"

    return render(request,'everything/home.html', {"title":title, "posts":posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.poster_id = current_user.id
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})