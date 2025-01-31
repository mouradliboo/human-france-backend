from  .models import AgentProfile
import  django_filters
from rest_framework import filters
class AgentListFilter(django_filters.FilterSet):
    agent_function = django_filters.CharFilter(field_name="agent_function",lookup_expr='iexact')
    ville = django_filters.CharFilter(field_name="ville",lookup_expr='iregex')
    status = django_filters.CharFilter(field_name="status",lookup_expr='exact')

    class Meta:
        model = AgentProfile
        fields = ['agent_function',"ville","status"]