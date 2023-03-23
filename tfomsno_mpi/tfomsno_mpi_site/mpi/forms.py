from django import forms

from .models import NsiMpiPolisType, NsiDudlType


class FormMpiGetPersonData(forms.Form):
    pcyType = forms.ModelChoiceField(
        label="Тип полиса",
        queryset=NsiMpiPolisType.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select",
            }
        )
    )
    enp = forms.CharField(
        min_length=16,
        max_length=16,
        label="ЕНП",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    pcySer = forms.CharField(
        max_length=5,
        label="Серия полиса старого образца",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    pcyNum = forms.CharField(
        max_length=10,
        label="Номер полиса старого образца",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    tmpcertNum = forms.CharField(
        min_length=9,
        max_length=9,
        label="Номер временного свидетельства",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )

    dudlSer = forms.CharField(
        max_length=5,
        label="Серия документа",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    dudlNum = forms.CharField(
        max_length=12,
        label="Номер документа",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    dudlType = forms.ModelChoiceField(
        label="Тип документа",
        queryset=NsiDudlType.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select",
            }
        )
    )

    snils = forms.CharField(
        min_length=14,
        max_length=14,
        label="Номер СНИЛС",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    birthDay = forms.DateField(
        label="Дата рождения",
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            }
        )
    )

    surname = forms.CharField(
        max_length=50,
        label="Фамилия",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    firstname = forms.CharField(
        max_length=50,
        label="Имя",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    patronymic = forms.CharField(
        max_length=50,
        label="Отчество",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    show = forms.CharField(
        max_length=50,
        label="Сущность",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            }
        )
    )
    dt = forms.DateField(
        label="Дата состояния",
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            }
        )
    )

    def clean_pcyType(self):
        if self.cleaned_data["pcyType"] is not None:
            pcy_code = NsiMpiPolisType.objects.get(caption=self.cleaned_data["pcyType"]).code
            return pcy_code
        else:
            return ""
    
    def clean_dudlType(self):
        if self.cleaned_data["dudlType"] is not None:
            dudl_code = NsiDudlType.objects.get(caption=self.cleaned_data["dudlType"]).code
            return dudl_code
        else:
            return ""