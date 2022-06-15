from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from imageupload.serializers import UploadedImageSerializerAdmin, UploadedImageSerializerBasic, UploadedImageSerializerPremium, UploadedImageSerializerEnterprise, UploadedImageX
from imageupload.models import UploadedImage # import our model

class UploadedImagesViewSet(viewsets.ModelViewSet):

    # serializer depends from user-group (for admin/staff there is permision for all data change)
    def get_serializer_class(self):
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
    
    # only logged users will get data
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
    
    # used in 'author' in all serializers
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


