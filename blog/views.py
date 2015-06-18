
from django.shortcuts import render_to_response, get_object_or_404
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
class EntryView(ListView):
    template_name = 'Entry/Entry.html'
    model = Entry


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Entry.objects.all()
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
