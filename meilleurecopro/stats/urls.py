from django.urls import path

from .views import Statistics, Advertisements

urlpatterns = [
    path("statistics/", Statistics.as_view(), name="statistics"),
    path("advertisements/", Advertisements.as_view(), name="advertisements"),
]
