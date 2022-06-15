from rest_framework import serializers
from imageupload.models import UploadedImage # Import our UploadedImage model

class UploadedImageSerializerAdmin(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    # here we can force-change data
    #author = serializers.CharField(source="owner.author", read_only=True)
    
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description', 'author', 'duration', 'create_date', 'expiry_date')
        read_only_fields = ('thumbnail200x200','thumbnail400x400', 'author', 'create_date', 'expiry_date', 'expiry_link')
        write_only_fields = ('image')

class UploadedImageSerializerBasic(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """

    class Meta:
        model = UploadedImage
        fields = ('image','thumbnail200x200', 'title', 'description') #pk out
        read_only_fields = ('thumbnail200x200', 'author')
        write_only_fields = ('image')

class UploadedImageSerializerPremium(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """

    class Meta:
        model = UploadedImage
        fields = ('image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description',) #pk out
        read_only_fields = ('thumbnail200x200', 'thumbnail400x400', 'author')

class UploadedImageSerializerEnterprise(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description')
        read_only_fields = ('thumbnail200x200',)

class UploadedImageX(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    
    class Meta:
            model = UploadedImage
            fields = ()
            read_only_fields = ('thumbnail200x200',)

#-------------------------------------------------------------------
# do wywalenia

from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from rest_framework.fields import CurrentUserDefault
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'account_name', 'users', 'created']
        read_only_fields = ['account_name']

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