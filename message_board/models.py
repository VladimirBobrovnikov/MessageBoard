from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

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


class Advertisement(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	title = models.CharField(max_length=64, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.CharField(
		max_length=2,
		choices=CHOICES_CATEGORY,
		default='TA'
	)
	content = RichTextUploadingField('Текст')

	class Meta:
		verbose_name = "advertisement"
		verbose_name_plural = "advertisements"

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s/" % self.id


class Reaction(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='reactions')
	text = models.TextField(blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=False)

	class Meta:
		verbose_name = "reaction"
		verbose_name_plural = "reactions"

	def approve(self):
		self.approved = True
		self.save()

	def del_instance(self):
		self.delete()
