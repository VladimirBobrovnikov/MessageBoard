from django.contrib import admin
from .models import (
	Advertisement,
	Reaction,
)
from .forms import AdvertisementForm


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
	form = AdvertisementForm
