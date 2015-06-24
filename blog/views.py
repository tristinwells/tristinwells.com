from bootstrap.views import DeleteView
from bootstrap.views import ListView
from bootstrap.views import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django_core.views.mixins.auth import LoginRequiredViewMixin

from blog.models import Entry


class EntryView(DetailView):
    template_name = 'blog/view_entry.html'
    model = Entry
    pk_url_kwarg = 'entry_id'

class LoginRequiredView(LoginRequiredViewMixin, TemplateView):
    template_name = 'blog/loginRequired.html'

class EntryDeleteView(DeleteView):
    template_name = 'blog/delete_entry.html'
    model = Entry


class EntriesView(ListView):
    template_name = 'blog/blog.html'
    model = Entry

class UpdateEntryView(UpdateView):
    template_name = 'bog/update_entry.html'
    fields = ['title', 'body', 'objects']

