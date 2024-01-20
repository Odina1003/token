from django.urls import path, re_path
from .views import books
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Learn Swagger documentation",
        default_version='v1',
        description="We are learning DRF & documenting our API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="django@djanog.django"),
        license=openapi.License(name="No License"),),
    public = True,
    permission_classes=(permissions.Allowany,),
)

ulrpatterns = [ 
    path('', books),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]