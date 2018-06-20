from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.friend_list, name='friend_list'),
    url(r'^(?P<pk>\d+)/$', views.friend_detail, name='friend_detail'),
]