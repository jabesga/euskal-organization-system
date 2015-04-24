from django.conf.urls import patterns, url
from gom import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       )
