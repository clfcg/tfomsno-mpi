# Generated by Django 4.1.7 on 2023-03-21 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpiServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('service_description', models.CharField(max_length=1000, verbose_name='Описание')),
                ('service_url', models.CharField(max_length=500, verbose_name='Адрес WSDL')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Сервис МПИ',
                'verbose_name_plural': 'Сервисы МПИ',
            },
        ),
        migrations.CreateModel(
            name='MpiMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meth_name', models.CharField(max_length=100)),
                ('meth_desc', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
                ('mpi_service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mpi.mpiservices')),
            ],
        ),
    ]
