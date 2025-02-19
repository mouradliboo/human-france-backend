
        
import django_filters
from .models import Planning,Conditions,PlanningAgent

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
        

class PositionnementFilter(django_filters.FilterSet):
    status = django_filters.NumberFilter(field_name="status", lookup_expr="icontains")  
    planning = django_filters.NumberFilter(field_name="planning", lookup_expr="icontains")
 
    class Meta:
        model = PlanningAgent
        fields = ['status','planning']
        
        