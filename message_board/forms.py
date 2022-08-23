from django.forms import ModelForm, CharField, Select, TextInput, Textarea
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Advertisement, CHOICES_CATEGORY, Reaction


class AdvertisementForm(ModelForm):
    category = CharField(label='Категория:', widget=Select(choices=CHOICES_CATEGORY))
    title = CharField(label='Заголовок', widget=TextInput(attrs={'class': 'form-control'}))
    content = CharField(label='Текст', widget=CKEditorUploadingWidget(attrs={'class': 'form-control'}))

    class Meta:
        model = Advertisement
        exclude = ('author',)


class ReactionForm(ModelForm):
    text = CharField(label='Текст', widget=Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Reaction
        fields = ('text',)
