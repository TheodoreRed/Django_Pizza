from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("", views.index, name="home"),
    path("new/", views.new_post, name="new-post"),
    path("info/", views.info, name="info"),
]
