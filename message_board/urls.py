from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    ReactionListView,
    ReactionUpdateView,
    ReactionCreateView,
    ReactionDetailView,
    confirm,
    delete_reaction,
)


urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_single'),
    path('create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('create/<int:pk>/', AdvertisementUpdateView.as_view(), name='advertisement_update'),

    path('<int:advertisement_pk>/reaction/', ReactionListView.as_view(), name='reaction_list'),
    path('<int:advertisement_pk>/reaction/create/', ReactionCreateView.as_view(), name='reaction_create'),
    path('<int:advertisement_pk>/reaction/create/<int:reaction_id>/', ReactionUpdateView.as_view(), name='reaction_update'),
    path('<int:advertisement_pk>/reaction/<int:reaction_id>/', ReactionDetailView.as_view(), name='reaction_single'),

    path('<int:advertisement_pk>/reaction/<int:reaction_id>/confirm', confirm, name='reaction_confirm'),
    path('<int:advertisement_pk>/reaction/<int:reaction_id>/delete', delete_reaction, name='reaction_delete'),
]
