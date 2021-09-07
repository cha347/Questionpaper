

import django_filters
from .models import Question
class FilterInformation(django_filters.FilterSet):
    class Meta:
        model=Question
        fields=['Department','Course','Semester']

