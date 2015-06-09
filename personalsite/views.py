from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class AddView(TemplateView):
    template_name = 'add-entry.html'
