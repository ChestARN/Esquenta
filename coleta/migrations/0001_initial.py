# Generated by Django 4.2.1 on 2023-05-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_material', models.CharField(help_text='Tipo de Material', max_length=50)),
                ('estado', models.CharField(help_text='Condições do Produto', max_length=50)),
                ('peso', models.FloatField(help_text='Peso do produto', max_length=20)),
                ('valor', models.DecimalField(decimal_places=10, help_text='Valor calculado pelo app', max_digits=10)),
            ],
        ),
    ]
