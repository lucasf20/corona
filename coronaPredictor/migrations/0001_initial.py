# Generated by Django 3.0.5 on 2020-04-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('cpf', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=10)),
                ('idade', models.IntegerField()),
                ('doenca', models.BooleanField()),
                ('nome_doenca', models.CharField(max_length=1000)),
                ('observacao', models.CharField(max_length=1000)),
            ],
        ),
    ]
