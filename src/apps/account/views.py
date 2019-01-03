# from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .models import User


# Create your views here.

def index(request):
    return HttpResponse('Index')

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)


    return HttpResponse('User ID: {}'.format(str(user), (user.age), (user.username)))



