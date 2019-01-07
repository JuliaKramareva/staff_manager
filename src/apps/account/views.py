# from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import User
from apps.account.forms import ProfileForm, Contact_us


# Create your views here.

def index(request):
    return HttpResponse('Index')

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = ProfileForm(instance=user)
    context = {'form': form}
    return render(request, 'account/profile.html', context=context)

def contact_us(request):


    if request.method == "GET":
        form = Contact_us()
    elif request.method == "POST":
        form = Contact_us(request.POST)
        if form.is_valid():
            form.save()
            # return redirect

    context = {'form': form}
    return render(request, 'account/contact_us.html', context=context)

    # return HttpResponse('User ID: {}'.format(str(user), (user.age), (user.username)))



