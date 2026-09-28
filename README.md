# LawyerSystem API

API RESTful de um escritório de advocacia, feita com Django + Django REST Framework.

## Domínio

| Entidade | Campos principais | Relacionamento |
|----------|-------------------|----------------|
| `Cliente` | nome, cpf_cnpj, email, telefone, endereco | 1:N com `Processo` |
| `Advogado` | nome, oab, email, telefone | 1:N com `Processo` |
| `Processo` | tipo, descricao, valor | FK para `Cliente` (obrigatória) e `Advogado` (opcional) |

Regras de integridade referencial:
- **Cliente** → `on_delete=PROTECT`: um cliente com processos não pode ser removido (retorna `400`).
- **Advogado** → `on_delete=SET_NULL`: ao remover o advogado, os processos dele ficam sem responsável.

## Como rodar

### 1. Ambiente virtual e dependências

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 2. Variáveis de ambiente

Copie o exemplo e ajuste os valores:

```bash
cp .env.example .env        # Windows: copy .env.example .env
```

| Variável | Descrição |
|----------|-----------|
| `SECRET_KEY` | Chave secreta do Django (obrigatória) |
| `DEBUG` | `True` ou `False` |
| `ALLOWED_HOSTS` | Hosts separados por vírgula |
| `DB_ENGINE` | `mysql` ou `sqlite` |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | Credenciais do MySQL (ignoradas no SQLite) |

Para usar MySQL, crie o banco antes:

```sql
CREATE DATABASE lawyersystem CHARACTER SET utf8mb4;
```

### 3. Migrações e servidor

```bash
python manage.py migrate
python manage.py runserver
```

A API fica em `http://127.0.0.1:8000/api/`. Abrindo no navegador, a interface do DRF
lista os recursos.

Testes: `python manage.py test core`

## Endpoints

Os três recursos (`clientes`, `advogados`, `processos`) seguem o mesmo padrão:

| Método | Rota | Ação | Sucesso |
|--------|------|------|---------|
| GET | `/api/<recurso>/` | Lista paginada (10 por página) | 200 |
| GET | `/api/<recurso>/<id>/` | Detalhe com dados relacionados aninhados | 200 |
| POST | `/api/<recurso>/` | Cria | 201 |
| PUT | `/api/<recurso>/<id>/` | Substitui por completo | 200 |
| PATCH | `/api/<recurso>/<id>/` | Atualiza parcialmente | 200 |
| DELETE | `/api/<recurso>/<id>/` | Remove | 204 |

Erros: `400` para payload inválido ou exclusão bloqueada, `404` para id inexistente e
`500` (em JSON) para erros não previstos.

### Filtros, busca e ordenação

- Clientes: `?cpf_cnpj=12345678901` · `?search=maria` · `?ordering=-nome`
- Advogados: `?oab=SC12345` · `?search=joao`
- Processos: `?cliente=1` · `?advogado=2` · `?advogado__isnull=true` · `?tipo__icontains=civ`
  · `?valor__gte=1000&valor__lte=3000` · `?ordering=-valor`
- Paginação: `?page=2`

### Serialização aninhada

Na leitura, `Processo` devolve `cliente` e `advogado` como objetos resumidos. Na escrita,
recebe só os ids:

```json
POST /api/processos/
{
  "tipo": "Trabalhista",
  "descricao": "Cobrança de horas extras",
  "valor": "1500.00",
  "cliente_id": 1,
  "advogado_id": 1
}
```

`Cliente` e `Advogado` devolvem a lista `processos` com um resumo de cada processo. Os
serializers resumidos (`core/serializers/resumo.py`) não incluem o lado de volta da
relação, então não há ciclo.

## Postman

A coleção `LawyerSystem.postman_collection.json` tem os requests de CRUD dos três
recursos e uma pasta "Erros esperados" com exemplos de 400 e 404.

## Estrutura

```
config/                 # settings, urls raiz
core/
  models/               # Cliente, Advogado, Processo
  serializers/          # ModelSerializers + resumos para aninhamento
  views/                # ModelViewSets com filtros
  urls.py               # DefaultRouter
  exceptions.py         # ProtectedError -> 400, erro inesperado -> 500 JSON
  tests/test_api.py
```
