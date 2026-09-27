from rest_framework import viewsets, filters

from ..models import Cliente
from ..serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome", "cpf_cnpj", "email"]
    ordering_fields = ["nome", "data_cadastro"]
