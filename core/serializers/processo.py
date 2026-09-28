from rest_framework import serializers

from ..models import Advogado, Cliente, Processo
from .resumo import AdvogadoResumoSerializer, ClienteResumoSerializer


class ProcessoSerializer(serializers.ModelSerializer):
    cliente = ClienteResumoSerializer(read_only=True)
    advogado = AdvogadoResumoSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        source="cliente",
        queryset=Cliente.objects.all(),
        write_only=True,
    )
    advogado_id = serializers.PrimaryKeyRelatedField(
        source="advogado",
        queryset=Advogado.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Processo
        fields = [
            "id",
            "tipo",
            "descricao",
            "valor",
            "cliente",
            "cliente_id",
            "advogado",
            "advogado_id",
            "data_cadastro",
        ]
        read_only_fields = ["id", "data_cadastro"]
