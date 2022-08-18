from django.contrib import admin
from .models import (
	Author,
	Advertisement,
	Text,
	File,
	Image,
	Video,
	Reaction,
)


# Register your models here.
class ImageInline(admin.TabularInline):
	model = Image


class VideoInline(admin.TabularInline):
	model = Video


class TextInline(admin.TabularInline):
	model = Text


class FileInline(admin.TabularInline):
	model = File


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
	list_display = ["author", "title", "updated", "category", "created"]
	list_display_links = ["title", ]
	list_filter = ["author", "title", "updated", "category", "created"]
	search_fields = ["title", "category", "updated", "timestamp"]
	inlines = [
		ImageInline,
		VideoInline,
		TextInline,
		FileInline,
	]

	class Meta:
		model = Advertisement


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ["id", "name"]
	list_editable = ["name"]
	search_fields = ["name"]

	class Meta:
		model = Category