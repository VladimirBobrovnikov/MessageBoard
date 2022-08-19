from django_filters import FilterSet, ModelChoiceFilter
from .models import Reaction, Advertisement
from django.contrib.auth import get_user_model


# создаём фильтр
class ReactionFilter(FilterSet):
	advertisement_choice = ModelChoiceFilter(
		field_name='author',
		queryset=Advertisement.objects.filter(author=get_user_model()),
		label='Объявление:'
	)

	class Meta:
		model = Reaction
		fields = {}
