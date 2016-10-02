import django_filters

from hotel.models import Deals


class DealsFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Deals
