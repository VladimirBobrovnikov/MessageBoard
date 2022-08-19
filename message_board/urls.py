from django.urls import path
from .views import AdvertisementListView, AdvertisementDetailView, AdvertisementCreateView, AdvertisementUpdateView


urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_single'),
    path('create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('create/<int:pk>/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
]
