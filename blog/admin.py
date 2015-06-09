from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from blog.models import Category
from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)

class ReadOnlyModelAdmin(ModelAdmin):
    """Read only model admin class that only allows reads."""

    readonly_fields = []

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if self.readonly_fields is None:
            self.readonly_fields = []

        fields = [field.name for field in obj._meta.fields
                  if field.name not in self.readonly_fields]
        return self.readonly_fields + fields

    def get_actions(self, request):
        actions = super(ReadOnlyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions