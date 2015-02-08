from django.conf.urls import patterns, url
from blurb import views


urlpatterns = patterns('',
    url(r'^random/$', views.random_blurb, name='random_blurb'),
    url(r'^(?P<slug>\w+)', views.genre_blurb, name="genre_blurb"),
    url(r'p/(?P<pk>\w+)', views.blurb_permalink, name="blurb_permalink"),
)

