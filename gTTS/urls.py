from django.urls import path
from .views import gTTs

urlpatterns = [
    path('<language>/<text>', gTTs),
]