from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from enderecos.api.serializers import EnderecoSerializer

class EnderecosViewSet(ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
