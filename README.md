# API com Django Rest Framework (DRF) + OAuth2

Este repositório contém a base de um projeto **Django Rest Framework (DRF)** com preparação inicial para implementação de **OAuth2** como mecanismo de autenticação.  
O objetivo é manter uma estrutura simples, clara e facilmente extensível à medida que novas funcionalidades forem adicionadas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Django 4.x  
- Django Rest Framework  
- Django OAuth Toolkit (futuramente)  
- SQLite (banco padrão, pode ser trocado posteriormente)

---

## 📦 Instalação e Configuração Inicial

Siga os passos abaixo para instalar o projeto localmente:

### 1️⃣ **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2️⃣ **Crie e Ative um Ambiente Virtual(venv)**
```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

### 3️⃣ **Instale às dependências iniciais**
```bash
pip install django djangorestframework
```

### 4️⃣ **Instale às dependências iniciais**
```bash
pip install django djangorestframework
```

### 4️⃣ **Instale a Biblioteca Responsável pelo Protocolo OaUTH2**
```bash
pip install django-oauth-toolkit
```

## 🔐 Introdução ao OAuth2

OAuth2 é um protocolo padrão de autorização usado para permitir que aplicações acessem recursos protegidos em nome de um usuário ou cliente.
Ele evita o compartilhamento direto de credenciais e trabalha com tokens de acesso.

## ⭐ Por que usar OAuth2?

Mais seguro que autenticação por login/senha via API

Permite diferentes tipos de aplicações (mobile, frontend, backend, serviços)

Suporte a controle refinado de permissões e expiração de tokens

## 🔑 Principais Fluxos do OAuth2
1. Authorization Code 

Ideal para aplicações web que possuem frontend e backend.
Fluxo mais seguro, pois o token é trocado no backend.

2. Implicit

Usado em antigos SPAs. Hoje é desencorajado devido a questões de segurança.

3. Password Grant

O usuário envia login/senha diretamente para a API.
Simples, porém menos seguro. Útil em sistemas internos.

4. Client Credentials

Aplicações servidor-servidor (APIs internas, microserviços).
Não envolve usuários, apenas serviços que se autenticam diretamente.

5. Refresh Token

Permite renovar o token de acesso sem pedir novamente login/senha.
Geralmente usado com Authorization Code e Password.