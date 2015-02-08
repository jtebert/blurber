from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blurber.views.index', name='index'),
    url(r'^about/$', 'blurber.views.about', name='about'),
    url(r'^blurb/', include('blurb.urls', namespace="blurb")),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
)