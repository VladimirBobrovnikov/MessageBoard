from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'Автор: {self.user.username}'


class Advertisement(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='advertisements')
	title = models.CharField(max_length=64, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.CharField(
		max_length=2,
		choices=[
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
		],
		default='TA'
	)
	content = RichTextUploadingField()

	class Meta:
		verbose_name = _("advertisement")
		verbose_name_plural = _("advertisements")


class ItemBase(models.Model):
	owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	content_object = GenericForeignKey("content_type", "object_id")

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


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
