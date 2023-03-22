from django.urls import path

from .views import *


urlpatterns = [
    path("", index, name="mpi"),
    path("mpi/getPersonData/", GetPersonData.as_view(), name="get_person_data"),
]