# Generated by Django 5.0.1 on 2024-02-16 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0003_alter_funcionario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]
