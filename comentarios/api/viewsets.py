from rest_framework.viewsets import ModelViewSet
from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario

class ComentariosViewSet(ModelViewSet):

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer