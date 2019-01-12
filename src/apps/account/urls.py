from django.urls import include, path
from apps.account.views import index, user_profile, contact_us, Tos_View, FAQ_View, Request_Day_Off_View

app_name = 'account'
urlpatterns = [
    path('index/', index),
    path('contact_us/', contact_us, name='contact_us'),
    path('faq/', FAQ_View, name='faq'),
    path('tos/', Tos_View, name='tos'),
    path('profile/<int:user_id>', user_profile, name='profile'),

]