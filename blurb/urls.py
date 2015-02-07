from django.conf.urls import patterns, include, url

from blurb import views


urlpatterns = patterns('',
    url(r'^random/$', views.random_blurb, name='random_blurb'),
    url(r'^(?P<pk>\w+)/$', views.genre_blurb, name="genre_blurb"),
    url(r'p/(?P<pk>\w+)/', views.blurb_permalink, name="blurb_permalink"),

    # TEMPORARY
url(r'^$', views.temp_blurb, name='temp_blurb'),
)