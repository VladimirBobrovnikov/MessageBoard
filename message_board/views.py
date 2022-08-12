from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import (
	Advertisement,
	Text,
	File,
	Image,
	Video,
	Reaction
)

# Create your views here.
class AdvertisementListView(ListView):
	model = Advertisement
	template_name = 'advertisement_search.html'
	context_object_name = 'advertisement'
	queryset = Advertisement.objects.order_by('-updated')
	paginate_by = 10
