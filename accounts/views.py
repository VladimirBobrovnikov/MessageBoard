from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = 'login'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/account.html'
    form_class = UserCreationForm

    def get_object(self, **kwargs):
        username = self.request.user.username
        return User.objects.get(username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
