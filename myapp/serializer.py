from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # many to return in array format
        many = True
        model = Category
        # __all__ in order to get all the data fields 
        fields = '__all__'

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        # many to return in array format
        many = True
        model = Movies
        # __all__ in order to get all the data fields 
        fields = '__all__'

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        # many to return in array format
        many = True
        model = Signature
        # __all__ in order to get all the data fields 
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        # many to return in array format
        many = True
        model = Users
        # __all__ in order to get all the data fields 
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        # many to return in array format
        many = True
        model = Favorite
        # __all__ in order to get all the data fields 
        fields = '__all__'