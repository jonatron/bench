from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^foo/$', views.FooList.as_view()),
    url(r'^foocreate/$', views.FooGetCreate.as_view()),
]
