from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

from user.permissions import IsAdmin
from expertise.models import Expertise
from expertise.serializers import ExpertiseSerializer, ExpertiseModelSerializer

class ExpersiteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
    ):
    serializer_class = ExpertiseSerializer

    def get_permissions(self):
        permission_clases = [IsAuthenticated]

        return [permission() for permission in permission_clases]

    def create(self, request, *args, **kwargs):
        serializer = ExpertiseSerializer(data=request.data, context={"request": self.request})
        serializer.validate(raise_exception=True)
        expertise = serializer.save()
        data = ExpertiseModelSerializer(expertise).data

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Expertise.objects.all()
        return queryset
