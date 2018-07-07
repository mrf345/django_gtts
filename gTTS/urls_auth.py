from django.urls import path
from .views import gTTs_auth

urlpatterns = [
    path('<language>/<text>', gTTs_auth)
]