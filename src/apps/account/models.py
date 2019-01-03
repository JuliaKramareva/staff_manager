from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=False)  #TODO validate age >=18.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    telephone = models.CharField('telephone', max_length=12, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()




    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'telephone'


    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     telephone = models.CharField(max_length=15, blank=True, null=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()









