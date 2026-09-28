from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from ..models import Cliente
from ..serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.prefetch_related("processos")
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["cpf_cnpj"]
    search_fields = ["nome", "cpf_cnpj", "email"]
    ordering_fields = ["nome", "data_cadastro"]
