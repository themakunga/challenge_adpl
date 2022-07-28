from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

from user.permissions import IsAdmin
from area.models import Area
from area.serializers import AreaModelSerializer, AreaSerializer

class AreaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
    ):
    serializer_class = AreaModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsAdmin]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = AreaSerializer(data=request.data, context={"request": self.request})
        serializer.validate(raise_exception=True)
        area = serializer.save()

        data = AreaModelSerializer(area).data

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Area.objects.all()
        return queryset
