from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink

from .managers import BlogEntryManager


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_dttm = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category', blank=True, null=True)
    created_user = models.ForeignKey(User)
    objects = BlogEntryManager()

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

