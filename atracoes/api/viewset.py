from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    default_filter_backends = [DjangoFilterBackend, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['nome']
    # filter_fields = ('nome', 'descricao')