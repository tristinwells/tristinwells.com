from datetime import datetime

from bootstrap.views import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Entry


# Class based views:
# TemplateView
# ListView
# DetailView
# FormView
# class EntryView(TemplateView):
#     template_name = 'Entry.html'
# class EntryIndex(ListView):
#     # queryset = Entry.objects.published()
#     template_name = "home.html"
#     paginate_by = 2
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

class EntryListView(ListView):

    model = Entry

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
