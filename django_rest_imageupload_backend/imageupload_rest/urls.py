from django.conf.urls import url, include
from rest_framework import routers
from .views import UploadedImagesViewSet


router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')

urlpatterns = [
    url(r'^', include(router.urls)),
]