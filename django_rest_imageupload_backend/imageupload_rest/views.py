from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from imageupload.serializers import UploadedImageSerializerAdmin, UploadedImageSerializerBasic, UploadedImageSerializerPremium, UploadedImageSerializerEnterprise, UploadedImageX
from imageupload.models import UploadedImage # import our model
#from django.conf import settings
#from django.db import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.conf import settings

class UploadedImagesViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        #if self.request.user.is_staff:
        if self.request.user.groups.filter(name="Basic").exists():
            return UploadedImageSerializerBasic
        elif self.request.user.groups.filter(name="Premium").exists():
            return UploadedImageSerializerPremium
        elif self.request.user.groups.filter(name="Enterprise").exists():
            return UploadedImageSerializerEnterprise
        elif self.request.user.is_staff:
            return UploadedImageSerializerAdmin
            #request.user.groups.all() 
        return UploadedImageX
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        try:
            return UploadedImage.objects.filter(author=user)
        except:
            return UploadedImage.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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