# Dumbledore Chat API

Uma API Flask que proporciona uma experiência de chat imersiva com Alvo Dumbledore, utilizando o modelo DeepSeek para criar conversas autênticas dentro do universo Harry Potter.

## Requisitos

- Python 3.11+
- Conta e chave de API no OpenRouter
- Dependências:

```bash
pip install flask requests python-dotenv gunicorn
```

## Configuração da API

1. Clone o repositório
2. Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_api_openrouter
```

3. Execute a aplicação:

```bash
python main.py
```

## Endpoints

### POST /

Endpoint principal para chat com Dumbledore.

**Primeira conversa (novo usuário):**
```json
{
    "nome": "Pedro",
    "content": "Oi, professor."
}
```

**Conversas subsequentes:**
```json
{
    "content": "Qual meu nome?",
    "session_id": "e71b77c5-6cf7-4d00-8a1f-4abe202dda41"
}
```

**Resposta:**
```json
{
    "resposta": "Ah, meu caro bruxo Pedro, é sempre um prazer recebê-lo em meu gabinete. Como diretor de Hogwarts, estou aqui para orientá-lo em sua jornada mágica.",
    "session_id": "e71b77c5-6cf7-4d00-8a1f-4abe202dda41"
}
```

**Resposta de erro:**
```json
{
    "erro": "Faltam informações.",
    "fields": ["None id", "None nome", "None content"]
}
```

## Estrutura do Projeto

```
DumbChat/
├── main.py          # Arquivo principal da aplicação Flask
├── route.py         # Definição das rotas
├── chat.py          # Lógica de comunicação com DeepSeek
├── requirements.txt # Dependências do projeto
├── Dockerfile       # Configuração Docker
├── .env            # Variáveis de ambiente (criar)
└── README.md       # Este arquivo
```

## Como Funciona

A API utiliza o modelo DeepSeek através do OpenRouter para gerar respostas como Dumbledore. O sistema:

1. Identifica se é uma nova conversa (com `nome`) ou continuação (com `session_id`)
2. Analisa o nome do usuário para determinar o tratamento adequado
3. Mantém contexto através de session IDs únicos
4. Retorna respostas em formato canônico do universo Harry Potter

## Características do Dumbledore

- Respostas sempre em duas frases
- Tratamento baseado no gênero inferido do nome
- Vocabulário exclusivamente canônico de Harry Potter
- Tom sereno, sábio e levemente enigmático
- Nunca inventa feitiços ou criaturas não-canônicos

## Deploy

### Local
```bash
python main.py
# Servidor rodando em http://127.0.0.1:5000
```

### Docker
```bash
docker build -t dumbledore-api .
docker run -p 5000:5000 dumbledore-api
```

### Produção (Render)
A aplicação está configurada para deploy automático no Render com:
- Gunicorn como servidor WSGI
- 4 workers para melhor performance
- Porta 5000 exposta

## Exemplos de Uso

### Primeira interação
```bash
curl -X POST https://dumblechatapi.onrender.com/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "Pedro", "content": "Oi, professor."}'
```

### Continuação da conversa
```bash
curl -X POST https://dumblechatapi.onrender.com/ \
  -H "Content-Type: application/json" \
  -d '{"content": "Qual meu nome?", "session_id": "seu-session-id"}'
```

## Limitações

- Usa modelo gratuito do DeepSeek (pode ter limitações de rate)
- Sessões não são persistidas entre reinicializações
- Focado exclusivamente no universo Harry Potter canônico