# app urls
from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

schema_view = get_schema_view(
    openapi.Info(
        title="BLOGGR API",
        default_version="v1",
        description="Lets Talk!",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        path(
            "docs/",
            schema_view.with_ui("redoc", cache_timeout=None),
            name="schema-redoc",
        ),
        path(
            "docs/live/",
            schema_view.with_ui("swagger", cache_timeout=None),
            name="schema-swagger",
        ),
    ]


urlpatterns += router.urls
