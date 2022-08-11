from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Advertisement(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
	title = models.CharField(max_length=64, blank=False)
	create_datetime = models.DateTimeField(auto_now_add=True)
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
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	file = models.FileField(upload_to='files/', null=True, blank=True)

	class Meta:
		verbose_name = _("advertisement")
		verbose_name_plural = _("advertisements")


class Reaction(models.Model):
	id = models.AutoField(primary_key=True)
	advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='reactions')
	text = models.TextField(blank=False)
	create_datetime = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	class Meta:
		verbose_name = _("reaction")
		verbose_name_plural = _("reactions")

	def approve(self):
		self.approved = True
		self.save()

	def del_instance(self):
		pass
