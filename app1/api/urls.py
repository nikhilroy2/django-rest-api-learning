from django.urls import path
from . import views
urlpatterns = [
    path('personal', views.PersonalAPI, name="personal"),
    path('personal/<int:pk>', views.PersonalAPI, name="personal_put")
]