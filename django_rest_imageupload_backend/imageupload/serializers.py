from email.policy import default
from rest_framework import serializers
from imageupload.models import UploadedImage # Import our UploadedImage model
from django.contrib.auth.models import User

# Serializer for UploadedImage Model
# serializes pk and image
class UploadedImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    # Create a custom method field
    #current_user = serializers.SerializerMethodField('_user')
    
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description', 'author')
        read_only_fields = ('thumbnail200x200',)

class UploadedImageSerializerBasic(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    # Create a custom method field
    #current_user = serializers.SerializerMethodField('_user')
    
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = UploadedImage
        fields = ('thumbnail200x200', 'title', 'description',)
        read_only_fields = ('thumbnail200x200',)

class UploadedImageSerializerPremium(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    # Create a custom method field
    #current_user = serializers.SerializerMethodField('_user')
    
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description',)
        read_only_fields = ('thumbnail200x200',)

class UploadedImageSerializerEnterprise(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    # Create a custom method field
    #current_user = serializers.SerializerMethodField('_user')
    
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description',)
        read_only_fields = ('thumbnail200x200',)





    


# dodanie użytkowników
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import Group
UserModel = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ('password', 'username', 'email', 'is_staff', 'groups',)

#dodanie grup
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
UserModel = get_user_model()

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)