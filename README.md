

# 🔐 FastAPI JWT HTTPS Lab

[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/release/python-3120/)
[![Last Commit](https://img.shields.io/github/last-commit/danilocasabona/fastapi-jwt-https-lab)](https://github.com/danilocasabona/fastapi-jwt-https-lab/commits/main)
[![License](https://img.shields.io/github/license/danilocasabona/fastapi-jwt-https-lab)](LICENSE)

Este é um laboratório prático criado para demonstrar a implementação de **autenticação com JWT (JSON Web Tokens)**, usando **FastAPI**, **HTTPS com certificado autoassinado** e **boas práticas de segurança para APIs REST**
---

## ✅ Objetivos do projeto:

- Login de usuário com envio seguro de **usuário e senha via Body (JSON)**
- Geração de **token JWT com expiração**
- Proteção de rotas via **Authorization Header (Bearer Token)**
- Exposição de documentação interativa via **Swagger UI com esquema de segurança HTTP Bearer**
- Execução em ambiente **HTTPS local** com **certificados autoassinados**
- Laboratório de testes práticos: token válido, token inválido e ausência de token

---

## ✅ Preparação do ambiente local (Python + VirtualEnv)

1. **Criar o ambiente virtual:**

```bash
python3 -m venv venv
```

2. **Ativar o ambiente virtual:**

- **Mac/Linux:**
```bash
source venv/bin/activate
```

- **Windows:**
```bash
venv\Scripts\activate
```

3. **Instalar as dependências:**

```bash
pip install -r requirements.txt
```

---

## ✅ Gerando certificados autoassinados (para HTTPS local):

Execute no terminal:

```bash
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes
```

👉 Isso criará a pasta `/certs` com os arquivos:

- `cert.pem`
- `key.pem`

---

## ✅ Rodando a aplicação local com HTTPS:

```bash
uvicorn app.main:app --reload --ssl-keyfile=certs/key.pem --ssl-certfile=certs/cert.pem
```

A API estará disponível em:

```
https://localhost:8000
```

Documentação interativa Swagger:

```
https://localhost:8000/docs
```

---

## ✅ Testando o fluxo JWT:

1. **Login:**

- Endpoint: `POST /login`
- Body:

```json
{
  "username": "danilo",
  "password": "123"
}
```

(Usuário de teste definido no código)

---

2. **Obter o token JWT de resposta**

Exemplo:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

3. **Acessar rota protegida:**

- Endpoint: `GET /protegido`
- Header:

```
Authorization: Bearer <seu_token>
```

Ou, no Swagger UI, clique em **"Authorize"**, cole o token.

---

## ✅ Próximos passos sugeridos:

- Implementar **Refresh Token**
- Salvar usuários em banco real (ex: SQLite, PostgreSQL)
- Implementar controle de roles
- Adicionar testes unitários
- Automatizar com CI/CD

---

📌 **Este projeto faz parte do meu laboratório pessoal de estudos em Segurança de Aplicações e APIs.**

**Danilo Casabona**  
[https://www.linkedin.com/in/danilocasabona/](https://www.linkedin.com/in/danilocasabona/)