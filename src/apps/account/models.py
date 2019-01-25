from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps import model_choices as mch



class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)  # TODO validate age >= 18
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=8)
    city = models.ForeignKey('account.City', on_delete=models.SET_NULL, blank=True, null=True, related_name='users')

    vacation_days = models.PositiveSmallIntegerField(null=False,
                                                     blank=False,
                                                     default=0)
    sickness_days = models.PositiveSmallIntegerField(null=False,
                                                     blank=False,
                                                     default=0)

    @property
    def is_hr(self):
        return self.groups.filter(name='HR').exists()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class RequestDayOff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dayoffs')
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add
    date_from = models.DateTimeField(null=False, blank=False)
    date_to = models.DateTimeField(null=False, blank=False)
    type = models.PositiveSmallIntegerField(
        null=False, blank=False,
        choices=mch.REQUEST_TYPES,
        default=mch.REQUEST_SICKNESS,
    )
    reason = models.CharField(max_length=256, blank=True, null=True, default=None)  # reason required when status = REJECTED
    status = models.PositiveSmallIntegerField(
        null=False, blank=False,
        choices=mch.STATUSES,
        default=mch.STATUS_PENDING,
    )

    # TODO
    # override save method, if date_from > date_to -> raise IntegrityError('error message') (from db)
    # override __str__ (DO NOT USE self.user)
    # def __str__(self):
    #     return self.user.email  # extra DB call NEVER DO THIS!!!




class City(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


    # def get_full_name(self):
    #     full_name = '{}{}'.format(self.first_name, self.last_name)
    #     return full_name.strip()

class Contact_us(models.Model):
    email_from = models.CharField(max_length=56)
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=500)


class Faq(models.Model):
    pass


class Tos(models.Model):
    i_agree = models.BooleanField()

class Request_Day_Off(models.Model):
    pass
    # from
    # to
    # user
    # type=choice
    # confirmed