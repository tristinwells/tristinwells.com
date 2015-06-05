from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django_core.utils.random_utils import random_alphanum

from blog.models import Entry


class Command(BaseCommand):
    help = ("Creates superuser, creates non-superuser, creates 3 blog posts "
            "from non-super user")

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, username=None, *args, **options):
        self.superuser(username=username)
        user, created = self.non_superuser(username=username)
        self.create_blog_entries(user=user)

    def superuser(self, username):
        user, created = User.objects.get_or_create(
            username='{0}-admin'.format(username),
            first_name='Tristin'
        )

        if not user.is_superuser:
            user.is_superuser = True
            user.is_staff = True
            user.save()

        return user

    def non_superuser(self, username):
        defaults = {
            'first_name': 'Tristin',
            'last_name': 'Wells'
        }
        return User.objects.get_or_create(
            username=username,
            defaults=defaults
        )

    def create_blog_entries(self, user):
        entry1 = Entry.objects.create(
            title='title',
            slug='title-{0}'.format(random_alphanum()),
            body='content',
            created_user=user)
        entry2 = Entry.objects.create(
            title=('title kal jdfalkd klsjdals kfjaklfjaskdljfklfjsj fkajsflk'
                   'sjflkdsjf slkdjflkdj lk'),
            slug='title-{0}'.format(random_alphanum()),
            body='content',
            created_user=user
        )
        entry3 = Entry.objects.create(
            title='title-3',
            slug='title-{0}'.format(random_alphanum()),
            body='content',
            created_user=user
        )
        print('added 3 new blog entries for: {0}'.format(user.username))


        # TODO: create blog enties
#             defaults={'blog 1': date(2015, 5, 20),
#                       'blog 2': date(2015, 5, 30),
#                       'blog 3': date(2015, 5, 25)})


