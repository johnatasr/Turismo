from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True, read_only=False)
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)

    descricao_completa = SerializerMethodField()

    read_only_field = ('comentarios', 'avalicoes', 'atracoes')

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

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        return ponto

    def get_descricao_completa(self, obj):
        return '%s -- %s' % (obj.nome, obj.descricao)