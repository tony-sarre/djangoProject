from django.urls import path, include
from rest_framework import routers

from sac import views
from sac.views import AlertViewSet, AlertListViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('alerts', AlertViewSet)
router.register('alert-lists', AlertListViewSet)

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.login, name="login"),
    path("logout/", views.logout, name="logout")

]
