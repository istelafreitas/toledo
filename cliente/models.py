from django.db import models

class Cadastro(models.Model):
    nome = models.CharField('Nome do cliente:', max_length=100)
    cpf = models.CharField('CPF:', max_length=11)
    rg = models.CharField('RG:', max_length=8, blank=True, null=True)
    endereco = models.CharField('Endereço:', max_length=100)
    bairro = models.CharField('Bairro:', max_length=100)
    numero = models.CharField('n°:', max_length=100, blank=True, null=True)
    cidade = models.CharField('Cidade:', max_length=100)
    estado = models.CharField('Estado:', max_length=2)
    telefone = models.CharField('Telefone:', max_length=10, blank=True, null=True)
    celular = models.CharField('Celular:', max_length=11)
    email = models.EmailField('Email:', blank=True, null=True)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)


    def __str__(self):
        return self.nome
