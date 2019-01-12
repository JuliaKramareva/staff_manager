from django.forms import ModelForm

from apps.account.models import User, Contact_us, Tos, Faq


class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'first_name', 'last_name',
            'city'
        ]
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


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
