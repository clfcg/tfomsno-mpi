from django.shortcuts import render


def index(request):
    content = {
        "title": "Мастер Пациент Индекс",
        "content": "Все получилось",
    }
    return render(request, "mpi/index.html", content)
