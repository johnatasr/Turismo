from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class PontoTuristico(models.Model):

    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete= models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def aprovado_descricao(self):
        if self.aprovado == True:
            ap = 'Aprovado'
            desc = self.descricao
        else:
            ap = 'Reprovado'
            desc = self.descricao
        return '%s -- %s'%(ap,desc)

    def __str__(self):
        return self.nome