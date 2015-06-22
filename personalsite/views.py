from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class AddView(FormView):
    template_name = 'blog/add-entry.html'
