from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^salvation/gospel/book1/', views.book1, name='book1'),
    url(r'^salvation/AboutUs/', views.AboutUs, name='AboutUs'),
    url(r'^salvation/gospel/', views.gospel, name='gospel'),
    url(r'^salvation/', views.salvation, name='salvation'),
    ]
