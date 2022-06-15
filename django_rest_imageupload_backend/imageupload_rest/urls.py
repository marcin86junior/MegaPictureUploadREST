from django.conf.urls import url, include
from rest_framework import routers
from .views import UploadedImagesViewSet

router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]