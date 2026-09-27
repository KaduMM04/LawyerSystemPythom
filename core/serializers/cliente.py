from rest_framework import serializers

from ..models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
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
        ]
        read_only_fields = ["id", "data_cadastro"]
