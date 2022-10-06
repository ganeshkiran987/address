from rest_framework import serializers
from getaddress.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('uuid','latitude','longitude')
    def __init__(self, *args, **kwargs):
        super(AddressSerializer, self).__init__(*args, **kwargs)
    def validate(self, attrs):
        latitude = attrs.pop('latitude')
        if latitude:
            attrs['latitude'] = latitude
        else:
            raise serializers.ValidationError({'latitude':[('Latitude field required')]})
        longitude = attrs.pop('longitude')
        if longitude:
            attrs['longitude'] = longitude
        else:
            raise serializers.ValidationError({'longitude': [('Longitude field required')]})
        return attrs
        def create(self, validated_data):
            return Address.objects.create(**validated_data)