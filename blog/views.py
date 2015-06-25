from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
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

class LoginRequiredView(LoginRequiredViewMixin, TemplateView):
    template_name = 'blog/loginRequired.html'

class AddView(CreateView):
    model = Entry
    template_name = 'blog/add-entry.html'
    form_class = EntryAddForm

    def get_form_kwargs(self):
        form_kwargs = super(AddView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def get_success_url(self):
        return reverse('entry_view', args=[self.object.id])

class EntryDeleteView(DeleteView):
    template_name = 'blog/delete_view.html'
    model = Entry
    pk_url_kwarg = 'entry_id'
    success_url = reverse_lazy('blog_view')

class EntriesView(ListView):
    template_name = 'blog/blog.html'
    model = Entry
    pk_url_kwarg = 'entry_id'


class UpdateEntryView(UpdateView):
    form_class = EntryUpdateForm
    template_name = 'bog/update_entry.html'
    fields = ['title', 'body', 'objects']
