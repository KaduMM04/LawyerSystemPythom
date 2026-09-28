from django.core.validators import MinValueValidator
from django.db import models

from .advogado import Advogado
from .cliente import Cliente


class Processo(models.Model):
    tipo = models.CharField(max_length=80, verbose_name="Tipo do processo")
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="processos",
    )
    
    # se o advogado sair, o processo continua existindo sem responsável
    advogado = models.ForeignKey(
        Advogado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="processos",
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "processos"
        verbose_name = "Processo"
        verbose_name_plural = "Processos"
        ordering = ["-data_cadastro"]

    def __str__(self):
        return f"{self.tipo} - {self.cliente.nome}"
