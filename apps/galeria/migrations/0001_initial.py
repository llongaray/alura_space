# Generated by Django 5.0.3 on 2024-03-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('legenda', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('foto', models.CharField(max_length=200)),
            ],
        ),
    ]
