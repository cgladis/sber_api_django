# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ClientDataView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/clients/<int:id>/data/<str:type>', ClientDataView.run_post)
]
