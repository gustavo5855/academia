# Generated by Django 2.2.5 on 2019-09-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0004_auto_20190928_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichaexercicio',
            name='repeticoes',
            field=models.CharField(default=None, max_length=2, null=True, verbose_name='Repetições'),
        ),
        migrations.AddField(
            model_name='fichaexercicio',
            name='series',
            field=models.CharField(default=None, max_length=1, null=True, verbose_name='Séries'),
        ),
    ]
