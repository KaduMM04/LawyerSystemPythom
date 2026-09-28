from rest_framework import serializers

from ..models import Advogado
from .resumo import ProcessoResumoSerializer


class AdvogadoSerializer(serializers.ModelSerializer):
    processos = ProcessoResumoSerializer(many=True, read_only=True)

    class Meta:
        model = Advogado
        fields = [
            "id",
            "nome",
            "oab",
            "email",
            "telefone",
            "data_cadastro",
            "processos",
        ]
        read_only_fields = ["id", "data_cadastro"]
