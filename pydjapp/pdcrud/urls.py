from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pdcrud/
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
]