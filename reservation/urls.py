from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reservation import views

router = DefaultRouter()
router.register(r'reservation', views.ReservartionViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls))
]
