# Generated by Django 3.0.5 on 2020-04-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
