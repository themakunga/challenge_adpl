from rest_framework import serializers

from expertise.models import Expertise

class ExpertiseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = (
            'name',
        )

class ExpertiseSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=64)

    def create(self, data):
        expertise = Expertise.objects.get_or_create(**data)
        return expertise
