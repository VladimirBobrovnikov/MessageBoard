from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse


from .models import (
	Advertisement,
	Reaction
)
from .forms import AdvertisementForm, ReactionForm
from .filters import ReactionFilter


# Create your views here.
class AdvertisementListView(ListView):
	model = Advertisement
	template_name = 'message_board/advertisements.html'
	context_object_name = 'advertisements'
	queryset = Advertisement.objects.order_by('-updated')
	paginate_by = 3


class AdvertisementDetailView(DetailView):
	model = Advertisement
	template_name = 'message_board/advertisement.html'
	context_object_name = 'advertisement'


class AdvertisementCreateView(CreateView):
	template_name = 'message_board/advertisement_create.html'
	form_class = AdvertisementForm

	def get_success_url(self):
		return reverse('advertisement_list')

	def form_valid(self, form):
		advertisement = form.save(commit=False)
		user = self.request.user
		advertisement.author = user
		return super().form_valid(form)


class AdvertisementUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'advertisement.change_advertisement'
	template_name = 'message_board/advertisement_create.html'
	form_class = AdvertisementForm

	def get_object(self, **kwargs):
		advertisement_id = self.kwargs.get('pk')
		return Advertisement.objects.get(pk=advertisement_id)

	def get_success_url(self):
		return reverse('advertisement_list')

	def form_valid(self, form):
		messages.success(self.request, 'Запись успешно обновлена!')
		return super().form_valid(form)


class ReactionListView(ListView):
	model = Reaction
	template_name = 'message_board/reaction_list.html'
	context_object_name = 'reactions'
	queryset = Reaction.objects.order_by('-updated')

	def get_filter(self):
		return ReactionFilter(self.request.GET, queryset=super().get_queryset())

	def get_queryset(self):
		qs = self.get_filter().qs
		return qs.filter(advertisement__id=self.kwargs['advertisement_pk'])

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		filter = self.get_filter()
		context['filter'] = filter
		return context


class ReactionCreateView(CreateView):
	template_name = 'message_board/reaction_create.html'
	form_class = ReactionForm

	def get_success_url(self):
		return reverse('advertisement_list')

	def form_valid(self, form):
		reaction = form.save(commit=False)
		user = self.request.user
		reaction.author = user
		advertisement_id = self.kwargs['advertisement_pk']
		reaction.advertisement = Advertisement.objects.get(pk=advertisement_id)
		return super().form_valid(form)


class ReactionUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'reaction.change_reaction'
	template_name = 'message_board/reaction_create.html'
	form_class = ReactionForm

	def get_object(self, **kwargs):
		reaction_id = self.kwargs.get('reaction_id')
		return Reaction.objects.get(pk=reaction_id)

	def get_success_url(self):
		return reverse('advertisement_list')

	def form_valid(self, form):
		messages.success(self.request, 'Отклик успешно обновлен!')
		return super().form_valid(form)


class ReactionDetailView(DetailView):
	model = Reaction
	template_name = 'message_board/reaction.html'
	context_object_name = 'reaction'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		context['user'] = user
		return context


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

