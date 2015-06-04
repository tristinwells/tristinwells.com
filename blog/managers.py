from django.db import models


class BlogEntryManager(models.Manager):

    def get_by_user(self, user):
        return self.filter(created_user=user)

    def get_recent(self):
        return self.order_by('-posted')

    def get_by_month(self, month):
        return self.filter(pub_date='month')

    def get_by_day(self):
        return self.filter(pub_date='day')
