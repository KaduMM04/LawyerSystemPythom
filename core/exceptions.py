import logging

from django.db.models import ProtectedError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # Erros que o DRF já conhece (400 de validação, 404, 405...) seguem o padrão.
    response = exception_handler(exc, context)
    if response is not None:
        return response

    # DELETE de um registro protegido por on_delete=PROTECT.
    if isinstance(exc, ProtectedError):
        return Response(
            {"detail": "Registro possui processos vinculados e não pode ser removido."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    logger.exception("Erro não tratado", exc_info=exc)
    return Response(
        {"detail": "Erro interno do servidor."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
