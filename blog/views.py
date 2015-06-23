from bootstrap.views import DeleteView
from bootstrap.views import ListView
from django.views.generic.detail import DetailView

from blog.models import Entry


class EntryView(DetailView):
    template_name = 'blog/view_entry.html'
    model = Entry
    pk_url_kwarg = 'entry_id'

class EntryDeleteView(DeleteView):
    template_name = 'blog/delete_entry.html'
    model = Entry


class EntriesView(ListView):
    template_name = 'blog/blog.html'
    model = Entry


