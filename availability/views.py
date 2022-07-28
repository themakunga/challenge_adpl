from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from user.permissions import IsActiveMentor

from availability.serializers import AvailabilityModelSerializer, AvailabilitySerializer

class AvailabilityViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
    ):
    serializer_class = AvailabilityModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsActiveMentor]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = AvailabilitySerializer(data=request.data, context={"request": self.request})
        serializer.validate(rasise_exception=True)
        availability = serializer.save()
        data =  AvailabilityModelSerializer(availability).data

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Availability.objects.all()
        return queryset
