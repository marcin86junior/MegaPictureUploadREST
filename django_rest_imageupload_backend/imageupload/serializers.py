from rest_framework import serializers
from imageupload.models import UploadedImage

class UploadedImageSerializerAdmin(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the all data fields for admin
    """
    
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description', 'author', 'duration', 'create_date', 'expiry_date')
        read_only_fields = ('thumbnail200x200','thumbnail400x400', 'author', 'create_date', 'expiry_date', 'expiry_link')
        write_only_fields = ('image')

class UploadedImageSerializerBasic(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides: thumbnail200x200, title and description for basic group
    """

    image = serializers.ImageField(write_only=True)
    class Meta:
        model = UploadedImage
        fields = ('image', 'thumbnail200x200', 'title', 'description') #pk out
        read_only_fields = ('thumbnail200x200', 'author')
        write_only_fields = ('image')

class UploadedImageSerializerPremium(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides: image, thumbnail200x200, thumbnail400x400, title, description for premium group
    """

    class Meta:
        model = UploadedImage
        fields = ('image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description')
        read_only_fields = ('thumbnail200x200', 'thumbnail400x400', 'author')

class UploadedImageSerializerEnterprise(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides: image, thumbnail200x200, thumbnail400x400, title, description, author, duration, create_date, expiry_date for enterprise group
    """

    class Meta:
        model = UploadedImage
        fields = ('image', 'thumbnail200x200', 'thumbnail400x400', 'title', 'description', 'author', 'duration', 'create_date', 'expiry_date')
        read_only_fields = ('thumbnail200x200','thumbnail400x400', 'author', 'create_date', 'expiry_date', 'expiry_link')
        write_only_fields = ('image')

class UploadedImageSerializerCustom(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides: image, thumbnail200x200, thumbnail400x400, title, description, author, duration, create_date, expiry_date for enterprise group
    """

    class Meta:
        model = UploadedImage
        fields = ('image', 'title', 'description', 'author', 'duration', 'create_date', 'expiry_date', 'thumbnail_custom_size', 'thumbnail_custom_image')
        read_only_fields = ( 'author', 'create_date', 'expiry_date', 'expiry_link', )
        write_only_fields = ('image')
    
class UploadedImageX(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides "nothing" for not logged users and not-staff users
    """

    class Meta:
            model = UploadedImage
            fields = ()
            read_only_fields = ()