from django_filters import FilterSet, ModelChoiceFilter
from .models import Reaction, Advertisement
from django.contrib.auth import get_user_model


# создаём фильтр
class ReactionFilter(FilterSet):
	user = get_user_model()
	advertisement_choice = ModelChoiceFilter(
		field_name='author',
		queryset=Advertisement.objects.filter(author=user),
		label='Объявление:'
	)

	class Meta:
		model = Reaction
		fields = {}
