from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView

from .forms import FormMpiGetPersonData
from .utils import SOAPGetPersonData


def index(request):
    content = {
        "title": "Мастер Пациент Индекс",
        "content": "Все получилось",
    }
    return render(request, "mpi/index.html", content)


class GetPersonData(SOAPGetPersonData, FormView):
    form_class = FormMpiGetPersonData
    success_url = "#"
    template_name = "mpi/mpi_get_person_data.html"
    mixin_template_soap = "get_person_data.xml"

    def form_valid(self, form):
        self.mixin_cleaned_data = form.cleaned_data
        print(self.mixin_get_data())
        print(self.mixin_parse_response())
        return super().form_valid(form)