from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = EnderecoSerializer()

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 
                  'nome', 
                  'descricao',
                  'aprovado',
                  'foto',
                  'atracoes',
                  'avaliacoes',
                  'comentarios',
                  'endereco',
                  'descricao_completa'
                ]

    def get_descricao_completa(self, obj):
        return '%s -- %s' % (obj.nome, obj.descricao)