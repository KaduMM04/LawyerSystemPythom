from django.contrib import admin

from .models import Cliente, Advogado, Processo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf_cnpj", "email", "telefone", "data_cadastro")
    search_fields = ("nome", "cpf_cnpj", "email")


@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ("nome", "oab", "email", "telefone", "data_cadastro")
    search_fields = ("nome", "oab", "email")


@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "cliente", "advogado", "valor", "data_cadastro")
    list_filter = ("tipo",)
    search_fields = ("tipo", "descricao", "cliente__nome")
