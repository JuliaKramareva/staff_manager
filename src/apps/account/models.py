from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=False)  #TODO validate age >=18
    username = models.CharField(max_length=60, unique=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(max_length=64, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=60, default='')
    last_name = models.CharField(max_length=60, default='')
    age = models.PositiveSmallIntegerField(null=True)
    email = models.EmailField(blank=True, max_length=254)

    def __str__(self):
        return self.user.username

def create_profile(self, *args, **kwargs):
    u = super(User, self).save(*args, **kwargs)
    UserProfile.objects.get_or_create(user_id=u.id)
    return u



