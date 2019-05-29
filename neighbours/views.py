from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    title = "Neighborhoods"

    return render(request,'everything/home.html', {"title":title})
