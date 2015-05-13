from django.conf.urls import patterns, url
from gom import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^report-admin/$', views.send_mail_to_admin, name="send_mail_to_admin")
                       )
