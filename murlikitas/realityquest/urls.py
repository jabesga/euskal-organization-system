from django.conf.urls import patterns, url
from realityquest import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'mission/add-mission/$', views.add_mission, name="add_mission"),
                       url(r'mission/all/$', views.all_missions, name="all_missions"),
                       )
