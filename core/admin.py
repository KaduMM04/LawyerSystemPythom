from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf_cnpj", "email", "telefone", "data_cadastro")
    search_fields = ("nome", "cpf_cnpj", "email")
