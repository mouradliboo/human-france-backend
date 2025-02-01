
        
import django_filters
from .models import Planning

class PlanningListFilter(django_filters.FilterSet):
    filter_date = django_filters.CharFilter(field_name="updated_at", lookup_expr="icontains")  
    updated_at__gte = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="gte")  # Greater than or equal
    updated_at__lte = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="lte")  # Less than or equal

    class Meta:
        model = Planning
        fields = ['updated_at']

        
        