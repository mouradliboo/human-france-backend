
        
import django_filters
from .models import Planning,Conditions

class PlanningListFilter(django_filters.FilterSet):
    filter_date = django_filters.CharFilter(field_name="start_planning_date", lookup_expr="icontains")  
    updated_at__gte = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="gte")  # Greater than or equal
    updated_at__lte = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="lte")  # Less than or equal

    class Meta:
        model = Planning
        fields = ['updated_at']

class ConditionFilter(django_filters.FilterSet):
    planning = django_filters.NumberFilter(field_name="planning", lookup_expr="icontains")  
 
    class Meta:
        model = Conditions
        fields = ['planning']
        
        