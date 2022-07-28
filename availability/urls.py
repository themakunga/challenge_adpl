from django.urls import path, include
from rest_framework.routers import DefaultRouter

from availability import views

router = DefaultRouter()
router.register(r'availability', views.AvailabilityViewSet, basename='availability')

urlpatterns = [
    path('', include(router.urls))
]
