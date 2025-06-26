# Python Quote API

Este projeto é uma API simples em Flask que retorna citações aleatórias a partir de um arquivo JSON. Também inclui uma interface web para consumir a API.

## Como rodar o projeto

### 1. Clone o repositório

```
git clone https://github.com/greathiago/python-quote-api.git
cd python-quote-api
```

### 2. Crie e ative o ambiente virtual (caso ainda não exista)

No Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Execute a aplicação Flask

```
python app.py
```

A API estará disponível em: http://127.0.0.1:5000/api/quote

### 5. Use a interface web

Abra o arquivo `index.html` no seu navegador para consumir a API e ver as citações.

---

- Certifique-se de que o arquivo `quotes.json` está presente na raiz do projeto.
- O botão "Nova Citação" na interface web faz uma requisição para a API e exibe uma nova citação aleatória.
