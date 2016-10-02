from collections import Counter

from rest_framework import generics
from rest_framework.response import Response

from hotel.filters import DealsFilter
from hotel.models import Deals
from hotel.pagination import StandardResultsSetPagination
from hotel.serializers import DealsSerializer


class DealsList(generics.ListAPIView):
    queryset = Deals.objects.all()
    serializer_class = DealsSerializer
    pagination_class = StandardResultsSetPagination
    filter_class = DealsFilter


class DealsStats(generics.GenericAPIView):

    def get(self, request):
        deals = Deals.objects.all()

        final_prices = []
        cities = []
        ratings = []

        for deal in deals:
            final_prices.append(deal.actual_price * (1 - deal.discount/100))
            cities.append(deal.location.split(",")[-2].strip())
            ratings.append(deal.rating)

        response = {
            'min_final_price': min(final_prices),
            'max_final_price': max(final_prices),
            'area_distribution': Counter(cities),
            'avg_rating': reduce(lambda x, y: x + y, ratings) / len(ratings)
        }
        return Response(response)


