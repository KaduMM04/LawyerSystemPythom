from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from ..models import Processo
from ..serializers import ProcessoSerializer


class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.select_related("cliente", "advogado")
    serializer_class = ProcessoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        "cliente": ["exact"],
        "advogado": ["exact", "isnull"],
        "tipo": ["exact", "icontains"],
        "valor": ["gte", "lte"],
    }
    search_fields = ["tipo", "descricao"]
    ordering_fields = ["valor", "data_cadastro"]
