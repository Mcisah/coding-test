from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

urlpatterns += staticfiles_urlpatterns()

