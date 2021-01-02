from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import satellite_add_list, satellite_add_details

urlpatterns = [
    path('add/', satellite_add_list, name="satellites_list"),
    path('add/<int:pk>/', satellite_add_details, name="satellites_details")
]

urlpatterns = format_suffix_patterns(urlpatterns)
