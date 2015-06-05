from django.contrib.auth.models import User
from django_core.utils.random_utils import random_alphanum


def create_user(username=None):
    """Create a new test user."""
    return User.objects.create(
        username=username or random_alphanum(),
        email='{0}@blah.com'.format(random_alphanum())
    )
