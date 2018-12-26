from django.core.management.base import BaseCommand, CommandError
from apps.account.models import User
import random
import string
import time
import names




class Command(BaseCommand):
    help = 'Create test data'
    # startdate = datetime.date(YYYY,MM,DD)
    domains = ["hotmail.com", "gmail.com", "mail.com", "yahoo.com", "icloud.com"]
    letters = string.ascii_lowercase[:12]



    def handle(self, *args, **options):
        User.objects.exclude(is_superuser=True).delete()
        for i in range(10_000):
            user = User.objects.create(
                id = id.random.choice(1, 10_000),
                password = password.random.choice(string.ascii_lowercase + string.digits),
                last_login = last_login.datetime.date(random.randint(2018,2018), random.randint(1,12), \
                                                      random.randint(1,28)),
                is_superuser = False,
                username = username.(''.join(random.choice(string.ascii_lowercase) for x in range(random.choice(1, 10))) + \
                                     ''.join(random.choice(string.digits) for z in range(random.choice(1, 100)))),
                first_name = first_name.get_first_name(),
                last_name = last_name.get_last_name(),
                email = email.  ,
                is_staff = True,
                is_active = True,
                date_joined = date_joined.datetime.date(random.randint(2017,2018), random.randint(1,12), random.randint(1,28)),
                age = age.random.choice(21, 65),
                groups = groups.  ,
                user_permissions = user_permissions.
            )