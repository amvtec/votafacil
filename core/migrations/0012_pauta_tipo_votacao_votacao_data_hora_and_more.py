# Generated by Django 5.1.6 on 2025-03-18 23:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_pauta_tipo_votacao_pauta_votacao_aberta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pauta',
            name='tipo_votacao',
            field=models.CharField(choices=[('simples', 'Maioria Simples'), ('absoluta', 'Maioria Absoluta'), ('qualificada', 'Maioria Qualificada (2/3)')], default='simples', max_length=20),
        ),
        migrations.AddField(
            model_name='votacao',
            name='data_hora',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='votacao',
            unique_together={('vereador', 'pauta')},
        ),
    ]
