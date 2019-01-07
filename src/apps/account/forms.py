from django.forms import ModelForm

from apps.account.models import User, Contact_us


class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'first_name', 'last_name',
            'city'
        ]

class Contact_us(ModelForm):

    class Meta:
        model = Contact_us
        fields = [
            'email_from', 'title',
            'text'
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
