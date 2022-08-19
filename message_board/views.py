from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import (
	Advertisement,
	Reaction
)
from .forms import AdvertisementForm


# Create your views here.
class AdvertisementListView(ListView):
	model = Advertisement
	template_name = 'message_board/advertisements.html'
	context_object_name = 'advertisements'
	queryset = Advertisement.objects.order_by('-updated')


class AdvertisementDetailView(DetailView):
	model = Advertisement
	template_name = 'message_board/advertisement.html'
	context_object_name = 'advertisement'


class AdvertisementCreateView(CreateView):
	template_name = 'message_board/advertisement_create.html'
	form_class = AdvertisementForm


class AdvertisementUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'advertisement.change_advertisement'
	template_name = 'message_board/advertisement_create.html'
	form_class = AdvertisementForm

	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return Advertisement.objects.get(pk=id)


class ReactionListView(ListView):
	pass


class ReactionDetailView(DetailView):
	pass


class ReactionCreateView(CreateView):
	pass

