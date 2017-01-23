from django.conf.urls import url


from .views import *
urlpatterns = [
    url(r'^home/',home),
    url(r'^upload/',upload, name='upload'),
    ]