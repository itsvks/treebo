from rest_framework import serializers

from hotel.models import Deals


class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals