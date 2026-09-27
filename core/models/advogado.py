from django.db import models


class Advogado(models.Model):
    """Advogado do escritório."""

    nome = models.CharField(max_length=150)
    oab = models.CharField(max_length=20, unique=True, verbose_name="Número da OAB")
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "advogados"
        verbose_name = "Advogado"
        verbose_name_plural = "Advogados"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
