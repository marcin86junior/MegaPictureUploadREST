from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from imageupload.serializers import UploadedImageSerializer, UploadedImageSerializerBasic # import our serializer
from imageupload.models import UploadedImage # import our model
#from django.conf import settings
#from django.db import models

class UploadedImagesViewSet(viewsets.ModelViewSet):
    #queryset = UploadedImage.objects.all()
    #queryset = UploadedImage.objects.filter(author='1')
    #if User.groups.filter(name='Basic').exists():
    #queryset = UploadedImage.objects.filter(author=User.objects.get(username='tomek').id)

    #queryset = UploadedImage.objects.filter(author='auth.User.id')
    #queryset = UploadedImage.objects.filter(author='auth.User')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UploadedImageSerializer
            #request.user.groups.all() 
        return UploadedImageSerializerBasic
    
    serializer_class = UploadedImageSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        try:
            return UploadedImage.objects.all()
        except:
            return UploadedImage.objects.none()

    #def get_serializer_class(self):
    #    if self.request.user.is_staff:
    #        return FullAccountSerializer
    #return BasicAccountSerializer
            
        


'''
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

'''
from imageupload.serializers import UserSerializer # Import our UploadedImage model
from django.contrib.auth.models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    #@action(detail=True)
    def group_names(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])

def get(self, request, format=None):
    """
    Return a list of all users.
    """
    usernames = [user.username for user in User.objects.all()]
    return Response(usernames)