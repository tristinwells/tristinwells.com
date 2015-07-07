from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django_core.views.mixins.auth import LoginRequiredViewMixin

from blog.forms import EntryAddForm
from blog.forms import EntryUpdateForm
from blog.models import Entry


class EntryView(DetailView):
    template_name = 'blog/view_entry.html'
    model = Entry
    pk_url_kwarg = 'entry_id'

    def get_context_data(self, *args, **kwargs):
        context = super(EntryView, self).get_context_data(*args, **kwargs)
        tags = self.object.tags.all()

        icon_class = None
        for tag in tags:
            tag_name = tag.name.lower()
            if tag_name == 'sports':
                icon_class = 'fa-futbol-o'
#             elif tag_name == 'sports':
#                 icon_class = 'fa-futbol-o'

            if icon_class is not None:
                break

        context['icon_class'] = icon_class
        return context



class AddView(LoginRequiredViewMixin, CreateView):
    model = Entry
    template_name = 'blog/add-entry.html'
    form_class = EntryAddForm

    def get_form_kwargs(self):
        form_kwargs = super(AddView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def get_success_url(self):
        return reverse('entry_view', args=[self.object.id])


class EntryDeleteView(LoginRequiredViewMixin, DeleteView):
    template_name = 'blog/delete_view.html'
    model = Entry
    pk_url_kwarg = 'entry_id'
    success_url = reverse_lazy('blog_view')


class EntriesView(ListView):
    template_name = 'blog/blog.html'
    model = Entry
    pk_url_kwarg = 'entry_id'
    paginate_by = 2


class UpdateEntryView(LoginRequiredViewMixin, UpdateView):
    form_class = EntryUpdateForm
    template_name = 'blog/update_entry.html'
    # fields = ['title', 'body', 'objects']
    pk_url_kwarg = 'entry_id'
    model = Entry

    def get_success_url(self):
        return reverse('entry_view', args=[self.object.id])

class TagEntriesView(ListView):
    model = Entry
    template_name = 'blog/tag_it.html'

    def get_queryset(self):
        query_set = super(TagEntriesView, self).get_queryset()
        # tag = self.request.GET.get('tag')
        return query_set.filter(tags__name=self.kwargs.get('tag_slug'))
