from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name="homepage")
]