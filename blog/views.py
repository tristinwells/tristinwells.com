
from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Blog
from blog.models import Category
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

# Class based views:
# TemplateView
# ListView
# DetailView
# FormView

# class BlogView(TemplateView):
#     template_name = 'blog.html'

# class BlogIndex(ListView):
#     # queryset = Entry.objects.published()
#     template_name = "home.html"
#     paginate_by = 2


class BlogView(ListView):
    template_name = 'blog/blog.html'
    model = Blog


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
