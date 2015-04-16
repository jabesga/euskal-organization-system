from django.conf.urls import patterns, url
from euskal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.auth_login, name="auth_login"),
    url(r'^logout/$', views.auth_logout, name="auth_logout"),
    url(r'^preferences/$', views.preferences, name="preferences"),
    url(r'^status/$', views.status, name="status"),
)
