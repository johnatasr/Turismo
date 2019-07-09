from rest_framework.serializers import ModelSerializer, Serializer
from core.models import PontoTuristico, Identificacao
from atracoes.models import Atracao
from enderecos.models import Endereco
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework.decorators import action


class IdentificaocaSerializer(ModelSerializer):
    class Meta :
        model = Identificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):

    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    identi = IdentificaocaSerializer()
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    descricao_completa = SerializerMethodField()
    read_only_field = ('avaliacoes', )

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
                  'identi'
                ]


    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        # avaliacoes = validated_data['avaliacoes']
        # del validated_data['avaliacoes']

        comentarios = validated_data['comentarios']
        del validated_data['comentarios']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['identi']
        del validated_data['identi']

        ponto = PontoTuristico.objects.create(**validated_data)

        self.cria_atracoes(atracoes, ponto)

        doci = Identificacao.objects.create(**doc)
        end = Endereco.objects.create(**endereco)


        ponto.comentarios.set(comentarios)
        # ponto.avaliacoes.set(avaliacoes)

        ponto.endereco = end
        ponto.identi = doci

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s -- %s' % (obj.nome, obj.descricao)


