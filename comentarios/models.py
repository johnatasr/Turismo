from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)


    # @property
    # def valida_aprovacao(self):
    #     if self.aprovado == True:
    #         str = 'Sim'
    #     else:
    #         str = 'Não'
    #
    #     return '%s' % str

    def __str__(self):
        return self.usuario.username

