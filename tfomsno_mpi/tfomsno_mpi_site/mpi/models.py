from django.db import models


class MpiServices(models.Model):
    service_name = models.CharField(max_length=150, verbose_name="Наименование")
    service_description = models.CharField(max_length=1000, verbose_name="Описание")
    service_url = models.CharField(max_length=500, verbose_name="Адрес WSDL")
    is_active = models.BooleanField(default=False, verbose_name="Активен")

    class Meta:
        verbose_name = "МПИ Сервис"
        verbose_name_plural = "МПИ Сервисы"

    def __str__(self):
        return self.service_name


class MpiMethods(models.Model):
    meth_name = models.CharField(max_length=100, verbose_name="Наименование")
    meth_desc = models.CharField(max_length=1000, verbose_name="Описание")
    mpi_service = models.ForeignKey(
        "MpiServices",
        on_delete=models.PROTECT,
        verbose_name="Сервис МПИ"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен")

    class Meta:
        verbose_name = "МПИ Метод"
        verbose_name_plural = "МПИ Методы"

    def __str__(self):
        return self.meth_name


class NsiSex(models.Model):
    caption = models.CharField(max_length=15, verbose_name="Наименование")

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "НСИ Пол"

    def __str__(self):
        return self.caption


class NsiMpiPolisType(models.Model):
    caption = models.CharField(max_length=100, verbose_name="Наименование")
    code = models.CharField(max_length=5, verbose_name="Код")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Тип полиса"
        verbose_name_plural = "МПИ Типы полисов"
        ordering = ["id"]

    def __str__(self):
        return self.caption


class NsiDudlType(models.Model):
    caption = models.CharField(max_length=150, verbose_name="Наименование")
    code = models.CharField(max_length=2, verbose_name="Код")
    m_ser = models.CharField(max_length=10, verbose_name="Маска серии")
    m_num = models.CharField(max_length=15, verbose_name="Маска номера")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Тип документа"
        verbose_name_plural = "НСИ Типы документов"
        ordering = ["code"]

    def __str__(self):
        return self.caption


class MpiShow(models.Model):
    caption = models.CharField(max_length=15, verbose_name="Наименование")
    desc = models.CharField(max_length=100, verbose_name="Описание сущности")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Элемент сущности"
        verbose_name_plural = "МПИ Список сущностей"
        ordering = ["id"]

    def __str__(self):
        return self.caption
