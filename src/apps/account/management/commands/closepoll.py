from django.core.management.base import BaseCommand, CommandError
from apps.account.models import User
from uuid import uuid4
import random
import string
import time
import names




class Command(BaseCommand):
    help = 'Create test data'

    # domains = ["hotmail.com", "gmail.com", "mail.com", "yahoo.com", "icloud.com"]
    # letters = string.ascii_lowercase[:12]
    # username_choice = ((''.join(random.choice.zip(string.ascii_lowercase, srting.digits) \
    #                             for x in range(random.choice(1, 10)))
    # permissions_staff = (("Can view user", "Can view content type", "Can view group", "Can view session"), )
    # GROUPS_STAFF = ["Administration", "Analytics", "Statisticians", "Developers", "Sales"]



    def handle(self, *args, **options):
        # print('1'*100)
        result = []
        for i in range(10000):
            username = str(uuid4())
            user = User(
            # User.objects.create(
                username=username,
                email = username + '@example.com',
                age = random.randint(12, 100),
                telephone = '111-1111-111'


        )
            result.append(user)
        User.objects.bulk_create(result)

        # for i in range(10000):
        #     user = User.objects.create(
                # password = password.random.choice(string.ascii_lowercase + string.digits),
                # last_login = last_login.datetime.date(random.randint(2018,2018), random.randint(1,12), \
                #                                       random.randint(1,28)),
                # is_superuser = False,
                # username = username.randome.choice(username_choice),
                # first_name = first_name.get_first_name(),
                # last_name = last_name.get_last_name(),
                # email = email.random.choice(last_name.get_last_name() + "@" + domains),
                # is_staff = True,
                # is_active = True,
                # date_joined = date_joined.datetime.date(random.randint(2017,2018), random.randint(1,12), \
                #                                         random.randint(1,28)),
                # age = age.random.choice(21, 65),
                # groups = groups.random.choice(GROUPS_STAFF),
                # user_permissions = user_permissions.permissions_staff

