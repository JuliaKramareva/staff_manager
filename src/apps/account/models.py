from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=False)  #TODO validate age >=18.

    telephone = models.CharField('telephone', max_length=12, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

# class Meta:
#     verbose_name = 'User'
#     verbose_name_plural = 'Users'
#
#
#     def __unicode__(self):
#         return self.user


    def get_full_name(self):
        full_name = '{}{}'.format(self.first_name, self.last_name)
        return full_name.strip()












