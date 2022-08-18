from django.forms import ModelForm, ModelChoiceField, CharField, Select, Textarea
from .models import Advertisement, Author, CHOICES_CATEGORY


class AdvertisementForm(ModelForm):
    author = ModelChoiceField(queryset=Author.objects.all(), label='Автор:')
    category = CharField(label='Категория:', widget=Select(choices=CHOICES_CATEGORY))
    title = CharField(label='Заголовок', max_length=255)
    text = CharField(label='Текст статьи', widget=Textarea())

    class Meta:
        model = Advertisement
        fields = [
            'author', 'category', 'title', 'text',
        ]