from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario

class ComentariosViewSet(ModelViewSet):

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['data']
    lookup_field = 'id'

# class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
#     def get_default_renderer(self, view):
#         return JSONRenderer()