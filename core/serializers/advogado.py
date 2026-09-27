from rest_framework import serializers

from ..models import Advogado


class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = [
            "id",
            "nome",
            "oab",
            "email",
            "telefone",
            "data_cadastro",
        ]
        read_only_fields = ["id", "data_cadastro"]
