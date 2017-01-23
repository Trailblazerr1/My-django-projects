from django.conf.urls import url,include
from . import views
from django.conf.urls import include



urlpatterns = [
 url(r'^create/$', views.image_create, name='create'),
]