from django.contrib import admin

from blog.models import Entry
from blog.models import Category


class EntryAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)