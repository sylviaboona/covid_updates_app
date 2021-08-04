from django.contrib import admin
from django.urls import path
from .views import covid_stats_view

urlpatterns = [
    path('', covid_stats_view),
]