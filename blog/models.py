from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

from .managers import BlogEntryManager


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_dttm = models.DateTimeField(db_index=True, default=datetime.utcnow)
    category = models.ForeignKey('blog.Category', blank=True, null=True)
    created_user = models.ForeignKey(User)
    objects = BlogEntryManager()

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super(Entry, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Contacts(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )

    email = models.EmailField()

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])
