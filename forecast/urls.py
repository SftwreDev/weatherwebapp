from django.urls import path


from .views import *


urlpatterns = [
    path("", ForecastView.as_view(), name="forecast")
]
