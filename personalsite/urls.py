"""personalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from blog.views import EntriesView
from blog.views import EntryDeleteView
from blog.views import EntryView
from personalsite.views import AboutView
from personalsite.views import HomeView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', HomeView.as_view(), name='home_view'),
    url(r'^about/?$', AboutView.as_view(), name='about_view'),
    url(r'^blog/?$', EntriesView.as_view(), name='blog_view'),
    url(r'^blog/(?P<entry_id>[0-9]+)/?$', EntryView.as_view(), name='entry_view'),
    url(r'^blog/(?P<entry_id>[0-9]+)/delete/?$', EntryDeleteView.as_view(), name='delete_entry_view'),
    # url(r'^$', TemplateView.as_view(template_name='todo/index.html')),
    # url(r'^$', views.BlogIndex.as_view(), name="index")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
