
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from blog.models import Category
from blog.forms    import ContactForm
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
class EntryView(ListView):
    template_name = 'Entry/Entry.html'
    model = Entry


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Entry.objects.all()[:5]
    })

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

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class LoginRequiredViewMixin(object):
    """Use this with CBVs to ensure user is logged in.
    Example:
    class MyView(LoginRequireViewMixin, TemplateView):
        # to view stuff
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredViewMixin, self).dispatch(*args, **kwargs)

class StaffRequiredViewMixin(LoginRequiredViewMixin):
    """Require a logged in Staff member."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied

        return super(StaffRequiredViewMixin, self).dispatch(request,
                                                            *args,
                                                            **kwargs)

class SuperuserRequiredViewMixin(LoginRequiredViewMixin):
    """Require a logged in user to be a superuser."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied

        return super(SuperuserRequiredViewMixin, self).dispatch(request,
                                                                *args,
                                                                **kwargs)