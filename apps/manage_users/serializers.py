# from django.core.serializers.python import Serializer
from rest_framework import serializers
from ..store_app.models import Users, Addresses

class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Addresses
    fields = ('name', 'street', 'street2', 'city', 'state', 'zip_code')

class UserSerializer(serializers.ModelSerializer):
  address = AddressSerializer(read_only=True)

  class Meta:
    model = Users
    fields = ('first_name', 'last_name', 'email', 'phone_num', 'password', 'address')