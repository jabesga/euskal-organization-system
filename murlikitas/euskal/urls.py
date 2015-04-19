from django.conf.urls import patterns, url
from euskal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^dashboard/$', views.dashboard, name="dashboard"),
                       url(r'^register/$', views.auth_register, name="register"),
                       url(r'^login/$', views.auth_login, name="auth_login"),
                       url(r'^status/$', views.status, name="status"),
                       url(r'^vote-group-name/$', views.vote_group_name, name="vote-group-name"),
                       url(r'^preferences/$', views.preferences, name="preferences"),
                       url(r'^logout/$', views.auth_logout, name="auth_logout"),
                       )
