from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers.address_serilaizers import AddressSerializer
from django.utils.translation import gettext as _
from geopy.geocoders import GoogleV3
from .models import Address

# Create your views here.

class AddressCreateView(generics.CreateAPIView):
    serializer_class = AddressSerializer
    success_message = _("Address Created Successfully")

class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    success_message = _("Address Listed Successfully")

    def get_queyset(self):
        lattitude = self.kwargs.get('lat',None)
        longitude = self.kwargs.get('long',None)
        geocoder = GoogleV3()
        location_list = geocoder.reverse(lattitude,longitude)
        location = location_list[0]
        address = location.address
        return address

class AddressUpdateView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    success_message = _("Address Updated Successfully")
    lookup_field = 'uuid'

class AddressDeleteView(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    success_message = _("Address Deleted Successfully")
    lookup_field = 'uuid'

class AddressRetrieveView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    success_message = _("Address Retrieved Successfully")
    lookup_field = 'uuid'



