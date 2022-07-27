from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from user import views as user_views

router = DefaultRouter()
router.register(r'user', user_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
