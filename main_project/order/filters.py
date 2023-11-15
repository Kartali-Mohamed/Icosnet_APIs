import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Order
        fields = ('title',)
