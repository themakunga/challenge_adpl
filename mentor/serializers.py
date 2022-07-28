from rest_framework import serializers

from mentor.models import Mentor
from user.models import User

from area.serializers import AreaSerializer

class MentorModelSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(read_only=True, many=True)
    class Meta:
        model = Mentor
        fields = (
            'user',
            'areas',
            'is_authorized',
        )

class MentorSerializer(serializers.Serializer):
    is_authorized  = serializers.BooleanField()
    user_id = serializers.IntegerField(
        source=User.pk
    )

    def create(self, data):
        mentor = Mentor.objects.get_or_create(**data)
        return mentor

