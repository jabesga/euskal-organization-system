from django.conf.urls import patterns, url
from gcontacts import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )