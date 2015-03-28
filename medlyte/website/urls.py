from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
    url(r'^create-account/$', views.create, name='create'),
    url(r'^$', views.index, name='index'),
)
