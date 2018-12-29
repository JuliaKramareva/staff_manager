from django.urls import include, path
from apps.account.views import index, user_profile

urlpatterns = [
    path('index/', index),
    path('profile/<int:id>/', views.user_profile),

]