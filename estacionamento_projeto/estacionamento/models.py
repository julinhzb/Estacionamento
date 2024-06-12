from django.db import models

class Cliente(models.Model):
    nome = models.TextField()
    cpf = models.TextField(unique=True)

class Veiculo(models.Model):
    placa = models.TextField(unique=True)
    cor = models.TextField()

class RegistroEstacionamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    vaga = models.IntegerField()
    data_agendamento = models.DateTimeField()
    horario_agendamento = models.TimeField()
