from django.urls import include, path
from apps.account.views import index, user_profile, contact_us

app_name = 'account'
urlpatterns = [
    path('index/', index),
    path('contact_us/', contact_us, name='contact_us'),
    path('faq/', contact_us, name='faq'),
    path('profile/<int:user_id>', user_profile),

]