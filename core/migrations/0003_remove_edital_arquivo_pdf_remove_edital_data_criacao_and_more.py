# Generated by Django 5.1.3 on 2024-12-12 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_edital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edital',
            name='arquivo_pdf',
        ),
        migrations.RemoveField(
            model_name='edital',
            name='data_criacao',
        ),
        migrations.AddField(
            model_name='edital',
            name='data_publicacao',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='edital',
            name='status',
            field=models.CharField(default='ativo', max_length=50),
        ),
        migrations.AlterField(
            model_name='edital',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='edital',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
