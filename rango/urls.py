from django.conf.urls import url
from rango import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^about', views.about, name='about')
]