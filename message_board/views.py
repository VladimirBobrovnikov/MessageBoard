from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import (
	Advertisement,
	Text,
	File,
	Image,
	Video,
	Reaction
)
from .filters import AdvertisementFilter
from .forms import AdvertisementForm

# Create your views here.
class AdvertisementListView(ListView):
	model = Advertisement
	template_name = 'message_board/advertisements.html'
	context_object_name = 'advertisements'
	queryset = Advertisement.objects.order_by('-updated')
	paginate_by = 10

	def get_filter(self):
		return AdvertisementFilter(self.request.GET, queryset=super().get_queryset())

	def get_queryset(self):
		qs = self.get_filter().qs
		return qs

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		filter = self.get_filter()
		context['filter'] = filter
		return context

	def post(self, request, *args, **kwargs):
		# берём значения для нового товара из POST-запроса, отправленного на сервер
		advertisement = request.POST['advertisement_now']
		text = request.POST['text']

		reaction = Reaction(
			user=self.request.user,
			advertisement=advertisement,
			text=text,
		)
		reaction.save()
		return super().get(request, *args, **kwargs)


class AdvertisementPersonListView(AdvertisementListView):
	template_name = 'message_board/advertisements.html'
	paginate_by = 10

	def get_filter(self):
		qs = super().get_queryset()
		qs = qs.filter(author=self.request.user)
		return AdvertisementFilter(self.request.GET, queryset=qs)


class AdvertisementDetailView(DetailView):
	model = Advertisement
	template_name = 'message_board/advertisement.html'
	context_object_name = 'advertisement'


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
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

