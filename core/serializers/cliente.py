from rest_framework import serializers

from ..models import Cliente
from .resumo import ProcessoResumoSerializer


class ClienteSerializer(serializers.ModelSerializer):
    processos = ProcessoResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = [
            "id",
            "nome",
            "cpf_cnpj",
            "email",
            "telefone",
            "endereco",
            "data_cadastro",
            "processos",
        ]
        read_only_fields = ["id", "data_cadastro"]
