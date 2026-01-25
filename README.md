# Secure API Auth

Sistema de autenticação seguro com **FastAPI + JWT**, desenvolvido como projeto de portfólio focado em **arquitetura backend**, **segurança de APIs**, **boas práticas de autenticação** e **estrutura profissional de projeto**.

Este projeto faz parte de uma trilha prática de aprendizado contínuo em:

* Backend
* Segurança de aplicações
* DevSecOps
* APIs modernas
* Arquitetura de software

## Objetivo do Projeto

Criar uma API real, segura e escalável que implemente:

* Autenticação JWT
* Login seguro
* Rotas protegidas
* Arquitetura modular
* Boas práticas de segurança
* Estrutura pronta para produção

Não é um projeto tutorial — é um **laboratório de aprendizado contínuo** e construção de portfólio.

## Arquitetura do Projeto

```
secure-api-auth/
│
├── app/
│   ├── main.py
│   ├── auth/
│   │   ├── routes.py
│   │   ├── jwt.py
│   │   ├── models.py
│   │   └── __init__.py
│   ├── users/
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── __init__.py
│   └── requirements.txt
│
└── README.md
```

## Funcionalidades Implementadas

### Autenticação

* Login com usuário e senha
* Geração de token JWT
* Validação de token

### API

* FastAPI
* Swagger automático (`/docs`)
* Health check (`/health`)

### Segurança

* JWT
* Separação de camadas
* Estrutura modular
* Preparado para RBAC

## Fluxo de Autenticação

1. Usuário envia credenciais (`/login`)
2. API valida usuário
3. Token JWT é gerado
4. Token é retornado
5. Token é usado para acessar rotas protegidas

## Tecnologias

* Python 3.13
* FastAPI
* Uvicorn
* JWT (python-jose)
* Pydantic

## Execução Local

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload
```

Acesse:

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

# Roadmap do Projeto

## Fase 1 — Base (Atual)

✔ Estrutura do projeto
✔ FastAPI
✔ JWT
✔ Login
✔ Geração de token
✔ Swagger
✔ Organização modular

## Fase 2 — Segurança Avançada

Rotas protegidas com dependências
Middleware de autenticação
Validação de token automática
Refresh token
Expiração e rotação de tokens
Blacklist de tokens

## Fase 3 — Usuários

Cadastro de usuário
Hash de senha (bcrypt)
Validação de senha forte
Roles (admin, user, guest)
RBAC (Role-Based Access Control)

## Fase 4 — Banco de Dados

PostgreSQL
SQLAlchemy
Migrations (Alembic)
Modelagem de usuários
Modelagem de permissões

## Fase 5 — Observabilidade

Logs estruturados
Monitoramento
Healthcheck avançado
Métricas
Tracing

## Fase 6 — DevSecOps

Docker
Docker Compose
CI/CD
Pipeline de segurança
SAST
DAST
Dependency Scan
Secrets Scan
Pipeline GitHub Actions

## Fase 7 — Cloud

Deploy em cloud
Infra as Code
Terraform
AWS
API Gateway
Load Balancer
Secrets Manager

## Objetivo Final

Criar uma **API segura de produção**, com:

* Autenticação robusta
* Arquitetura escalável
* Segurança real
* Pipeline automatizado
* Infraestrutura como código
* Observabilidade
* Padrões profissionais

## Status do Projeto

Em desenvolvimento contínuo

Este projeto evolui por versões, não por tutoriais.
Cada fase representa maturidade técnica real.

## Autor

**GIL0F**
Estudos em:

* Backend
* Segurança da Informação
* DevSecOps
* Cloud
* Arquitetura de Software

## Propósito

Este repositório existe para:

* Aprendizado real
* Construção de portfólio
* Evolução técnica
* Demonstração de arquitetura
* Desenvolvimento profissional
