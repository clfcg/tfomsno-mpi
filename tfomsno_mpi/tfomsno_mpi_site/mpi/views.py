from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import FormMpiGetPersonData
from .utils import SendPersonData


def index(request):
    content = {
        "title": "Мастер Пациент Индекс",
        "content": "Все получилось",
    }
    return render(request, "mpi/index.html", content)


class GetPersonData(SendPersonData, FormView):
    form_class = FormMpiGetPersonData
    template_name = "mpi/mpi_get_person_data.html"
    success_url = "/"
    mixin_data = {}

    def form_valid(self, form):
        print(self.get_mixin_data(form.cleaned_data))
        print(form.cleaned_data)
        return super().form_valid(form)