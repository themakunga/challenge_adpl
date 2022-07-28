from rest_framework import serializers

from area.models import Area

class AreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('name',)

class AreaSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=64)

    def create(self, data):
        area = Area.objects.get_or_create(**data)
        return area
