from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_ROOT

# from drf_yasg2.views import get_schema_view
# from drf_yasg2 import openapi
# from rest_framework import permissions
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('account/', include('account.urls')),
                  path('manager/', include('manager.urls')),
                  path('cars/', include('cars.urls')),
                  path('frontdesk/', include('frontdesk.urls')),
                  path('user/', include('users.urls')),
                  path('requests/', include('requests.urls')),
                  path('services/', include('services.urls')),
                  path('parts/', include('parts.urls')),
                  path('advisor/', include('advisor.urls')),
                  path('mechanic/', include('mechanic.urls')),
                  path('__debug__/', include('debug_toolbar.urls')),
                  # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  #     re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  #     re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  # path('watchman/',include('watchman.urls'))
              ] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
