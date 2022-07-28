from rest_framework import serializers

from reservation.models import Reservation
from user.models import User
from mentor.models import Mentor
from mentor.serializers import MentorModelSerializer
from user.serializers import UserModelSerializer

class ReservationModelSerializer(serializers.ModelSerializer):
    mentor = MentorModelSerializer(read_only=True, many=True)
    member = UserModelSerializer(read_only=True, many=True)

    class Meta:
        model = Reservation
        fields = (
            'mentor',
            'member',
            'start',
            'end',
        )

class ReservationSerializer(serializers.Serializer):
    mentor = serializers.IntegerField(source=Mentor.pk)
    member = serializers.IntegerField(source=User.pk)
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, data):
        reservation = Reservation.objects.get_or_create(**data)
        return reservation
