from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^accounts/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("docs/", include("docs.urls")),
    path("", include("user_app.api.urls")),
    path("", include("shop.urls", namespace="shop")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
