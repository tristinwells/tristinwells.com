from django.views import generic
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class BlogIndex(generic.ListView):
    # queryset = Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2
