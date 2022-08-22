from django.urls import path, include
from .views import UserUpdateView, BaseRegisterView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', include('allauth.urls')),
    path('account/', UserUpdateView.as_view(), name='personal_area'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(), name='signup'),
]
