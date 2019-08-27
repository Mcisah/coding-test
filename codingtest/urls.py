from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    path('', views.index),
    path("graphiql/", csrf_exempt(GraphQLView.as_view(graphiql=True)), name='graphiql'),
]

urlpatterns += staticfiles_urlpatterns()

