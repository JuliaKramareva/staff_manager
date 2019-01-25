from django.forms import ModelForm
from django.db.models import Q
from django import forms
from  apps import model_choices as mch

from apps.account.models import User, Contact_us, Tos, Faq, RequestDayOff



class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'first_name', 'last_name',
            'city',
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #TODO


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'password', 'salary'
        ]

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
# check if user exists in database
            if User.objects.filter(Q(email=cleaned_data['email']) |
                                   Q(username=cleaned_data['email'])).exists():
                raise forms.ValidationError('User already exists')

        return cleaned_data

        # def save(self, commit=True):
        #     instance = super().save(commit=False)
        #     instance.username = instance.email
        #     if commit:
        #         instance.save()
        #     return instance

class RequestDayOffForm(forms.ModelForm):
    class Meta:
        madel = RequestDayOff
        fields = ['type', 'date_from', 'date_to']

    def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user')
            super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            # from pdb import set_trace
            # set_trace()
            if cleaned_data['date_from'] > cleaned_data['date_to']:
                self.add_error('date_to',
                               'date_from cannot be greater than date_to')
            if cleaned_data['type'] != mch.REQUEST_DAYOFF:
                pass
            # 1 dayoff is only for one day (more is vacation)
            # 2 date_to should be less than date_from
            # 3 date_from - date_to (in days) should not be greater than 20 (do not count weekends)
            # 4 dayoffs/vacation cannot be more than user has (user.vacation >= days)
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
            return instance

class Contact_us(ModelForm):

    class Meta:
        model = Contact_us
        fields = [
            'email_from', 'title',
            'text'
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Faq_form(ModelForm):
    pass



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

class Tos_Form(ModelForm):
    fields = ['i_agree']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


