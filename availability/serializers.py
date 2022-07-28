from rest_framework import serializers

from mentor.models import Mentor
from availability.models import Availability

class AvailabilityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = (
            'mentor',
            'start',
            'end',
        )

class AvailabilitySerializer(serializers.Serializer):
    mentor = serializers.IntegerField(
        source=Mentor.pk
    )
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, data):
        availability = Availability.objects.get_or_create(**data)
        return availability
