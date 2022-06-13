from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters, permissions
from imageupload.serializers import UploadedImageSerializer # import our serializer
from imageupload.models import UploadedImage # import our model
from rest_framework.permissions import * #(AllowAny, IsAdminUser, IsAuthenticated, )

class UploadedImagesViewSet(viewsets.ModelViewSet):

    serializer_class = UploadedImageSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_groups = {
        'Basic': ['Developers'], # Developers can POST
        'partial_update': ['Designers','Developers'],  # Designers and Developers can PATCH
        'retrieve': ['_Public'], # retrieve can be accessed without credentials (GET 'site.com/api/foo/1')
        }

#
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

#
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)