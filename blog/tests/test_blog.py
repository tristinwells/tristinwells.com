from django.test import TestCase

from blog.models import Entry
from personalsite.tests.utils import create_user


# Create your tests here.
"""Make names relevant to what you are doing"""
class BlogPostTest(TestCase):
    """This tests to make sure there is at least one blog entry"""
    def test_create_unpublished(self):
        user = create_user()
        entry = Entry(title="Title Me", body="Hello world", created_user=user)
        entry.save()
        self.assertEqual(Entry.objects.all().count(), 1)
        entry.publish = True
        entry.save()
