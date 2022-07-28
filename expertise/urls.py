from django.urls import path, include
from rest_framework.routers import DefaultRouter

from expertise import views

router = DefaultRouter()
router.register(r'expertise', views.ExpersiteViewSet, basename='expertise')

urlpatterns = [
    path('', include(router.urls))
]
