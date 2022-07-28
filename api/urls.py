"""Main URLs module."""

from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="ADPList API Challenge",
      contact=openapi.Contact(email="nmartinez@icloud.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include(('user.urls', 'user'), namespace='user')),
    path('api/', include(('mentor.urls', 'mentor'), namespace='mentor')),
    path('api/', include(('availability.urls', 'availability'), namespace='availability')),
    path('api/', include(('reservation.urls', 'reservation'), namespace='reservation')),
    path('api/', include(('area.urls', 'area'), namespace='area')),
    path('api/', include(('expertise.urls', 'expertise'), namespace='expertise')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_obtain_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
