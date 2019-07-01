from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao
from enderecos.models import Endereco
from avaliacoes.models import Avaliacao
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(ModelSerializer):


    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    read_only_field = ('comentarios', 'atracoes')

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
                  'descricao_completa',
                  ''

                ]

    def cria_avaliacoes(selfs, avaliacoes, ponto ):
        for avaliacao in avaliacoes:
            av = Avaliacao.objects.create(**avaliacao)
            ponto.avaliacoes.add(av)

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        avaliacoes = validated_data['avaliacoes']
        del validated_data['validated_data']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        self.cria_avaliacoes(avaliacoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s -- %s' % (obj.nome, obj.descricao)