from datetime import datetime

from bootstrap.views import DeleteView
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Category
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

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)

        return context

class EntryDeleteView(DeleteView):
    template_name = 'blog/delete_entry.html'
    model = Entry


class EntriesView(ListView):
    template_name = 'blog/blog.html'
    model = Entry

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Entry, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Entry.objects.filter(category=category)[:5]
    })


class EntryListView(ListView):

    model = Entry

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
