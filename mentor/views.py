# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsActiveMentor
from mentor.models import Mentor
from mentor.serializers import MentorModelSerializer, MentorSerializer

class MentorViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    ):
    serializer_class = MentorModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsActiveMentor]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = MentorSerializer(data=request.data, context={"request": self.request})
        serializer.validate(raise_exception=True)
        mentor = serializer.save()
        data = MentorModelSerializer(mentor).data

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Mentor.objects.get()
        return queryset
