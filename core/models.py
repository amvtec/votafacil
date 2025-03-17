from django.db import models

# Modelos de Vereador
class Vereador(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    partido = models.CharField(max_length=50)
    senha = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos_vereadores/')
    funcao = models.CharField(max_length=50, choices=[('Vereador', 'Vereador'), ('Presidente', 'Presidente'), ('Vice-Presidente', 'Vice-Presidente'), ('Primeiro Secretário', 'Primeiro Secretário')])
    status = models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])
    
    def __str__(self):
        return self.nome


# Modelos de Sessão
from django.db import models

class Sessao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    arquivada = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20, 
        choices=[('Em Andamento', 'Em Andamento'), ('Arquivada', 'Arquivada')]
    )
    vereadores_presentes = models.ManyToManyField("Vereador", blank=True)  # ✅ Adicionado
    encerrada_em = models.DateTimeField(null=True, blank=True)  # ✅ Novo campo para armazenar a data e hora do encerramento

    def __str__(self):
        return self.nome



# Modelos de Pauta
class Pauta(models.Model):
    ORIGEM_CHOICES = [
        ('Executivo', 'Executivo'),
        ('Legislativo', 'Legislativo'),
    ]

    STATUS_CHOICES = [
        ('Em Espera', 'Em Espera'),
        ('Em Votação', 'Em Votação'),
        ('Aprovada', 'Aprovada'),
        ('Rejeitada', 'Rejeitada'),
        ('Encerrada', 'Encerrada'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    autor = models.ForeignKey("Vereador", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    sessao = models.ForeignKey("Sessao", on_delete=models.CASCADE)
    origem = models.CharField(max_length=20, choices=ORIGEM_CHOICES)
    arquivo_pdf = models.FileField(upload_to="pautas_pdfs/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Em Espera")

    # 🔹 Novo campo para definir se a votação é aberta ou fechada
    votacao_aberta = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo




    def definir_resultado(self):
        """
        Define automaticamente o resultado da votação com base nos votos.
        """
        votos_sim = self.voto_set.filter(voto="Sim").count()
        votos_nao = self.voto_set.filter(voto="Não").count()

        if votos_sim > votos_nao:
            self.status = "Aprovada"
        else:
            self.status = "Rejeitada"

        self.save()

    def __str__(self):
        return f"{self.titulo} - {self.status}"



# Modelos de Votação
class Votacao(models.Model):
    vereador = models.ForeignKey(Vereador, on_delete=models.CASCADE)
    pauta = models.ForeignKey(Pauta, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulo
    voto = models.CharField(
        max_length=10,
        choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Abstenção', 'Abstenção')],
        null=True,
        blank=True
    )
    presenca = models.BooleanField(default=False)  # Adiciona a presença aqui

    def __str__(self):
        return f"{self.vereador.nome} - {self.pauta if self.pauta else 'Presença'} - {self.voto if self.voto else 'Presente'}"



# Modelos de Relatório
class Relatorio(models.Model):
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    data_geracao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='relatorios/')

    def __str__(self):
        return f'Relatório da Sessão {self.sessao.nome}'


# Modelos de Cronômetro de Fala
class Cronometro(models.Model):
    vereador = models.ForeignKey(Vereador, on_delete=models.CASCADE)
    tempo_inicial = models.IntegerField()  # Em segundos
    tempo_restante = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('Iniciado', 'Iniciado'), ('Pausado', 'Pausado'), ('Finalizado', 'Finalizado')])
    data_inicio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cronômetro - {self.vereador.nome}'

class PresencaRegistrada(models.Model):
    sessao = models.ForeignKey('Sessao', on_delete=models.CASCADE)
    vereador = models.ForeignKey('Vereador', on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vereador.nome} - {self.sessao.nome}"


