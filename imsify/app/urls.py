
from django.conf.urls import url

from app import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^Developers/', views.Developers, name='Developers'),
	url(r'^playlist/', views.playlist, name='playlist'),

]
