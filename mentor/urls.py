from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mentor import views

router = DefaultRouter()
router.register(r'mentor', views.MentorViewSet, basename='mentor')

urlpatterns = [
    path('', include(router.urls))
]
