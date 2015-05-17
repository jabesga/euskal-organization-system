from django.conf.urls import patterns, url
from terminal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^command/$', views.command, name='command')
                       )