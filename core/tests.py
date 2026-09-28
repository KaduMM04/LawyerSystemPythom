from rest_framework import status
from rest_framework.test import APITestCase

from .models import Advogado, Cliente, Processo


class LawyerSystemTests(APITestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nome="Maria Silva", cpf_cnpj="12345678901")
        self.advogado = Advogado.objects.create(nome="João Souza", oab="SC12345")

    def test_criar_processo_com_ids(self):
        """POST /api/processos/ recebe ids e devolve cliente/advogado como objetos."""
        dados = {
            "tipo": "Trabalhista",
            "descricao": "Cobrança de horas extras",
            "valor": "1500.00",
            "cliente_id": self.cliente.id,
            "advogado_id": self.advogado.id,
        }

        resposta = self.client.post("/api/processos/", dados, format="json")

        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Processo.objects.count(), 1)
        self.assertEqual(resposta.data["cliente"]["nome"], "Maria Silva")
        self.assertEqual(resposta.data["advogado"]["oab"], "SC12345")

    def test_cpf_invalido_retorna_400(self):
        """CPF com pontuação não passa no RegexValidator do model."""
        dados = {"nome": "Carlos", "cpf_cnpj": "123.456.789-01"}

        resposta = self.client.post("/api/clientes/", dados, format="json")

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("cpf_cnpj", resposta.data)
        self.assertEqual(Cliente.objects.count(), 1) 

    def test_nao_apaga_cliente_com_processo(self):
        """on_delete=PROTECT: cliente com processo não pode ser removido."""
        Processo.objects.create(tipo="Cível", valor="500.00", cliente=self.cliente)

        resposta = self.client.delete(f"/api/clientes/{self.cliente.id}/")

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(Cliente.objects.filter(id=self.cliente.id).exists())