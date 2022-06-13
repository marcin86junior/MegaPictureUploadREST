from django.conf.urls import url, include
from rest_framework import routers
#from imageupload.views import UploadedImagesViewSet

#from .views import CreateUserView
from .views import *

router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')
#router.register('api/customer', CreateUserView, 'customer')
#router.register(r'users', UserViewSet)
#router.register(r'accounts', AccountViewSet)
router.register('users', UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]