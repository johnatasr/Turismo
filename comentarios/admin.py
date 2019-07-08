from django.contrib import admin
from . models import Comentario
from comentarios.actions import reprova_comentarios, aprova_comentarios


class ComentariosAdmin(admin.ModelAdmin):

    list_display = ['usuario', 'data', 'aprovado']
    actions = ['aprova_comentarios', 'reprova_comentarios']

admin.site.register(Comentario)