import os
from hashlib import md5

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from ckeditor_uploader.fields import RichTextUploadingField

from SF_Finall import settings

CHOICES_CATEGORY = [
	('TA', 'Танки'),
	('HL', 'Хилы'),
	('DD', 'ДД'),
	('MR', 'Торговцы'),
	('GM', 'Гилдмастеры'),
	('QG', 'Квестгиверы'),
	('BM', 'Кузнецы'),
	('TN', 'Кожевники'),
	('PM', 'Зельевары'),
	('SM', 'Мастера заклинаний'),
]


class Author(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'

	def __str__(self):
		return f'Автор: {self.user.username}'


class Category(models.Model):
	id = models.AutoField()
	name = models.CharField(
		max_length=2,
		choices=CHOICES_CATEGORY,
		default='TA'
	)

	class Meta:
		verbose_name = _("category")
		verbose_name_plural = _("categories")

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Advertisement(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='advertisements')
	title = models.CharField(max_length=64, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='advertisements')
	content = RichTextUploadingField()

	class Meta:
		verbose_name = _("advertisement")
		verbose_name_plural = _("advertisements")

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s/" % self.id


class ItemBase(models.Model):
	id = models.AutoField()
	advertisement = models.ForeignKey(Advertisement, blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	content_object = GenericForeignKey("content_type", "object_id")

	class Meta:
		abstract = True

	def get_absolute_url(self):
		return "/%s/" % self.id


class Text(ItemBase):
	content = models.TextField()


class File(ItemBase):
	file = models.FileField(upload_to='files')


class Image(ItemBase):
	file = models.FileField(upload_to='images')


class Video(ItemBase):
	video = models.FileField(upload_to='media')


class Reaction(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
	advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='reactions')
	text = models.TextField(blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=False)

	class Meta:
		verbose_name = _("reaction")
		verbose_name_plural = _("reactions")

	def approve(self):
		self.approved = True
		self.save()

	def del_instance(self):
		self.delete()
