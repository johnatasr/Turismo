from django.db import models

class Atracao(models.Model):

    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField('Horário de Funcionamento')
    idade_min = models.IntegerField('Idade Mínima')

    def __str__(self):
        return self.nome