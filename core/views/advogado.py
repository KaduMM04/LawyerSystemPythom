from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from ..models import Advogado
from ..serializers import AdvogadoSerializer


class AdvogadoViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.prefetch_related("processos")
    serializer_class = AdvogadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["oab"]
    search_fields = ["nome", "oab", "email"]
    ordering_fields = ["nome", "data_cadastro"]
