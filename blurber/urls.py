from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blurber.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('blurb.urls', namespace="blurb")),

    url(r'^admin/', include(admin.site.urls)),
)
