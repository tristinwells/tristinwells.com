from django.core.management.base import BaseCommand, CommandError
from entry.models import Entry

class Command(BaseCommand):
    help = "Creates superuser, creates non-superuser, creates 3 blog posts from non-super user"

    def handle(self, *args, **options):
        self.superuser()
        self.non_superuser()

    def superuser(self):
        obj, created = Person.objects.get_or_create(superuser='tristin-admin')

    def non_superuser(self):
        obj, created = Person.objects.get_or_create(
            superuser='tristin',
            defaults={'blog 1': date(2015, 5, 20),
                      'blog 2': date(2015, 5, 30),
                      'blog 3': date(2015, 5, 25)})

