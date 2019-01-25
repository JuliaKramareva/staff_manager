from django.urls import include, path
from apps.account.views import index, profile, contact_us, Tos_View, FAQ_View, create_request

app_name = 'account'
urlpatterns = [
    path('index/', index),
    path('contact_us/', contact_us, name='contact_us'),
    path('faq/', FAQ_View, name='faq'),
    path('tos/', Tos_View, name='tos'),
    path('profile/', profile, name='profile'),
    path('create-request/', create_request, name='create-request'),

]