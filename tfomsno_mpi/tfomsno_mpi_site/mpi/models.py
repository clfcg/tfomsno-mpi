from django.db import models


class MpiServices(models.Model):
    service_name = models.CharField(
        max_length=150, 
        verbose_name="Наименование"
    )
    service_description = models.CharField(
        max_length=1000,
        verbose_name="Описание"
    )
    service_url = models.CharField(
        max_length=500,
        verbose_name="Адрес WSDL"
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активен"
    )

    class Meta:
        verbose_name = "Сервис МПИ"
        verbose_name_plural = "Сервисы МПИ"