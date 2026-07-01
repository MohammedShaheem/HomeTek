from django.urls import path
from .views import social

urlpatterns = [
    path("",social),
]