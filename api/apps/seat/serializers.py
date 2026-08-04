from rest_framework import serializers
from apps.seat.models import Seat

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
