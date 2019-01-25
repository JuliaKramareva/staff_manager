# from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.account.models import User, Faq, Tos
from apps.account.forms import ProfileForm, Contact_us, Faq_form, Tos_Form, RequestDayOffForm


# Create your views here.

def index(request):
    from apps.account.tasks import send_email_async
    # task_number_one.delay()
    # task_number_one()

    # 1
    # send_email_async.delay(
    #     'Subject here',
    #     'Here is the message.',
    #     from_email='from@example.com',
    #     recipient_list=['to@example.com'],
    # )

    # 2
    send_email_async.async_call(
        args=('Subject here', 'Here is the message.'),
        kwargs={'from_email': 'from@example.com',
                'recipient_list': ['to@example.com']},
        countdown=60 * 45,  # 45 min
    )
    return HttpResponse('Index')


@login_required  # profile = login_required(profile)
def profile(request):
    user = request.user
    if request.method == "GET":
        form = ProfileForm(instance=user)
    elif request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:index'))

    context = {'form': form}
    return render(request, 'account/profile.html',
                  context=context)


@login_required
def create_request(request):
    user = request.user
    base_form = RequestDayOffForm

    if request.method == "GET":
        form = base_form(user=user)
    elif request.method == "POST":
        form = base_form(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:index'))
    context = {'form': form}
    return render(request, 'account/create-request.html',
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