from django.conf.urls import patterns, url
from api import views


urlpatterns = patterns('',
    url(r'genres/$', views.genres, name="genres"),
    url(r'(?P<slug>[\w-]+)/(?P<will_save>\d+)/$', views.genre_blurb, name="genre_blurb"),
    url(r'p/(?P<pk>\w+)/$', views.blurb_permalink, name="blurb_permalink"),
)