# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsActiveMentor
from reservation.models import Reservation
from reservation.serializers import ReservationModelSerializer, ReservationSerializer

class ReservartionViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    ):
    serializer_class = ReservationModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsActiveMentor]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data, context={"request": self.request})
        serializer.validate(raise_exception=True)
        mentor = serializer.save()
        data = ReservationModelSerializer(mentor).data

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Reservation.objects.all()
