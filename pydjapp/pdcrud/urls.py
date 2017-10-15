from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pdcrud/
    url(r'^$', views.readall, name='readall'),
    url(r'^index/$', views.create, name='create'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/([0-9]+)/$', views.update, name='update'),
    url(r'^readall/$', views.readall, name='readall'),
    url(r'^delete/([0-9]+)/$', views.delete, name='delete'),
]
