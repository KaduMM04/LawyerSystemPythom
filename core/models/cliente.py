from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
    """Cliente do escritório de advocacia."""

    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(
        max_length=18,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{11}$|^\d{14}$",
                message="Informe um CPF (11 dígitos) ou CNPJ (14 dígitos), somente números.",
            )
        ],
    )
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
