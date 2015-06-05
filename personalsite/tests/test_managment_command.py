from django.core.management import call_command
from django.test import TestCase
from django_core.utils.random_utils import random_alphanum

from blog.models import Entry
from personalsite.tests.utils import create_user


class BlogEntryManagerTest(TestCase):

    def test_create_blog_posts(self):
        # - get the user
        # self.non_superuser()
        user = create_user(username=random_alphanum())
        # - get the number of current blog posts
        count_before = Entry.objects.filter(created_user=user).count()
        # - run the management command
        call_command('datascript', user.username)
        # - assert that after the manamaement command has run that the user now
        #   has 3 more blog entries than they did before running the management
        #   command.
        count_after = Entry.objects.filter(created_user=user).count()
        self.assertEqual(count_after - count_before, 3)

        # .client.get('/management/')
        # self.assertEqual


"""
class HelloWorld(object):

    name = 'world'

    def add(self, num_1, num_2):
        return num_1 + num_2

    def get_hello(self):
        return self.name


>>> hw = HelloWorld()
>>> hw.get_hello()
'world'
>>> hw.add(5, 6)
11
>>> hw.name = 'tristin'
>>> hw.name
'tristin'
"""
