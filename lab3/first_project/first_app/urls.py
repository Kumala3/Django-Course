from django.urls import path

from .views import SkinsListView

urlpatterns = [
    path("skins/", SkinsListView)
]
