from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect

from .models import (
	Advertisement,
	Reaction
)
from .forms import AdvertisementForm
from .filters import ReactionFilter


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
	model = Reaction
	template_name = 'message_board/reaction_list.html'
	context_object_name = 'reactions'
	queryset = Reaction.objects.order_by('-updated')

	def get_filter(self):
		return ReactionFilter(self.request.GET, queryset=super().get_queryset())

	def get_queryset(self):
		qs = self.get_filter().qs
		return qs

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		filter = self.get_filter()
		context['filter'] = filter
		return context


class ReactionDetailView(DetailView):
	model = Reaction
	template_name = 'message_board/reaction.html'
	context_object_name = 'reaction'


def confirm(request):
	reaction_id = request.GET.get('reaction_id')
	reaction = Reaction.objects.get(id=reaction_id)
	user = request.user
	if reaction.advertisement.author == user:
		reaction.approve()

	return redirect('advertisement_list')


def delete_reaction(request):
	reaction_id = request.GET.get('reaction_id')
	reaction = Reaction.objects.get(id=reaction_id)
	user = request.user
	if reaction.advertisement.author == user:
		reaction.delete()

	return redirect('advertisement_list')

