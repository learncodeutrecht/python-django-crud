from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pdcrud/
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.create, name='create'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/([0-9]+)/$', views.update, name='update'),
    url(r'^readall/$', views.readall, name='readall'),
    url(r'^delete/([0-9]+)/$', views.delete, name='delete'),
	url(r'^select_single_thought/$', views.select_single_thought, name='select_single_thought'),
	url(r'^single_thought/([0-9]+)/$', views.view_single_thought, name='single_thought'),
	url(r'^delete_thought/$', views.delete_thought, name='delete_thought'),
	url(r'^update_thought/$', views.update_thought, name='update_thought'),
]
