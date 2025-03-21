# Generated by Django 5.1.6 on 2025-03-10 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('arquivada', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Em Andamento', 'Em Andamento'), ('Arquivada', 'Arquivada')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vereador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('partido', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='fotos_vereadores/')),
                ('funcao', models.CharField(choices=[('Vereador', 'Vereador'), ('Presidente', 'Presidente'), ('Vice-Presidente', 'Vice-Presidente'), ('Primeiro Secretário', 'Primeiro Secretário')], max_length=50)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_geracao', models.DateTimeField(auto_now_add=True)),
                ('arquivo', models.FileField(upload_to='relatorios/')),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sessao')),
            ],
        ),
        migrations.CreateModel(
            name='Pauta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('tipo', models.CharField(max_length=100)),
                ('origem', models.CharField(choices=[('Executivo', 'Executivo'), ('Legislativo', 'Legislativo')], max_length=20)),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sessao')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vereador')),
            ],
        ),
        migrations.CreateModel(
            name='Cronometro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo_inicial', models.IntegerField()),
                ('tempo_restante', models.IntegerField()),
                ('status', models.CharField(choices=[('Iniciado', 'Iniciado'), ('Pausado', 'Pausado'), ('Finalizado', 'Finalizado')], max_length=10)),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('vereador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vereador')),
            ],
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voto', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Abstenção', 'Abstenção')], max_length=10)),
                ('presenca', models.BooleanField(default=False)),
                ('pauta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pauta')),
                ('vereador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vereador')),
            ],
        ),
    ]
