from rest_framework import serializers

from ..models import Advogado, Cliente, Processo


class ClienteResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "cpf_cnpj"]


class AdvogadoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ["id", "nome", "oab"]


class ProcessoResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = ["id", "tipo", "valor"]
