# from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from apps.account.models import User, Faq, Tos
from apps.account.forms import ProfileForm, Contact_us, Faq_form, Tos_Form


# Create your views here.

def index(request):
    return HttpResponse('Index')


def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "GET":
        form = ProfileForm(instance=user)
    elif request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    # TODO check
    #url = reverse('account:profile', args=(user.id, ))
    #print(url)

    context = {'form': form, 'user': user}
    return render(request, 'account/profile.html',
                  context=context)
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

def FAQ_View(request):
    if request.method == "GET":
        form = Faq()
    elif request.method == "POST":
        form = Faq(request.POST)
        if form.is_valid():
            form.save()
            # return redirect

    context = {'form': form}
    return render(request, 'account/faq.html', context=context)

def Tos_View(request):
    if request.method == "GET":
        form = Tos()
    elif request.method == "POST":
        form = Tos(request.POST)
        if form.is_valid():
            form.save()
            # return redirect

    context = {'form': form}
    return render(request, 'account/tos.html', context=context)

def Request_Day_Off_View(request):
    pass