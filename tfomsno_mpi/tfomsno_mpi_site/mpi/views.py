from django.shortcuts import render
from django.views.generic import FormView

from .forms import FormMpiGetPersonData


def index(request):
    content = {
        "title": "Мастер Пациент Индекс",
        "content": "Все получилось",
    }
    return render(request, "mpi/index.html", content)


class GetPersonData(FormView):
    form_class = FormMpiGetPersonData
    template_name = "mpi/mpi_get_person_data.html"
