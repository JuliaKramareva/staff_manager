# from django.shortcuts import render
from django.http  import HttpResponse
from .models import UserProfile


# Create your views here.

def index(request):
    return HttpResponse('Index')

def user_profile(request):
    profile = request.user.get_profile()
    return profile



