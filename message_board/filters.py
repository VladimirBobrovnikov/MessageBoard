from django_filters import FilterSet, DateFilter, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Advertisement, Author, Category
from django.forms.widgets import SelectDateWidget


class AdvertisementFilter(FilterSet):
    author_choice = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Автор:')
    created__gte = DateFilter(field_name='date_time_in', lookup_expr='gte', label='Дата публикации (не ранее):', widget=SelectDateWidget)
    category_choice = ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all(), label='Категория:')

    class Meta:
        model = Advertisement
        fields = {}