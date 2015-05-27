from django.test import TestCase

from .models import Blog


# Create your tests here.
class BlogPostTest(TestCase):

    def test_create_unpublished(self):
        entry = Blog(title="Title Me", body=" ", publish=False)
        entry.save()
        self.assertEqual(Blog.objects.all().count(), 1)
        entry.publish = True
        entry.save()
