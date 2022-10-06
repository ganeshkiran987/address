from django.urls import path
from . import views
from getaddress.views import AddressCreateView,AddressListView,AddressUpdateView,AddressDeleteView,AddressRetrieveView

urlpatterns = [
    path('address/create/', AddressCreateView.as_view(),name="addresscreate"),
    path('address/list/', AddressListView.as_view(),name="addresslist"),
    path('address/update/<uuid:uuid>/', AddressUpdateView.as_view(),name="addressupdate"),
    path('address/destroy/<uuid:uuid>/', AddressDeleteView.as_view(),name="addressdelete"),
    path('address/retrieve/<uuid:uuid>/', AddressRetrieveView.as_view(),name="addressretrieve"),
]