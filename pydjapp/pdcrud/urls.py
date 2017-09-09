from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pdcrud/
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.create, name='create'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/([0-9]+)/$', views.update, name='update'),
    url(r'^readall/$', views.readall, name='readall'),
]
