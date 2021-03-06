"""oapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from product import views

routers = routers.DefaultRouter()
routers.register("product_info", views.ProductInfoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="运维工程API",
        default_version='v1.0',
        description='运维工程接口文档',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='admin@123.com'),
        license=openapi.License(name='Apache License')
    ),
    public=True,
    permission_classes=(permissions.DjangoModelPermissions, ),
)


urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('accounts/', xadmin.site.urls),
    path('admin/', xadmin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),

    path('api/', include(routers.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

    re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 图片url转发

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns