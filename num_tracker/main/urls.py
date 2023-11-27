from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("see-map", views.track_map, name="track_map"),
]
