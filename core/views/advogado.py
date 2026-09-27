from rest_framework import viewsets, filters

from ..models import Advogado
from ..serializers import AdvogadoSerializer


class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome", "oab", "email"]
    ordering_fields = ["nome", "data_cadastro"]
