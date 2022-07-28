from django.urls import path, include
from rest_framework.routers import DefaultRouter

from area import views

router = DefaultRouter()
router.register(r'area', views.AreaViewSet, basename='area')

urlpatterns = [
    path('', include(router.urls))
]
