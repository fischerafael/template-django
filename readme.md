## create venv

python -m venv venv

## activate venv

venv\Scripts\activate

## install django and drf

pip install django django_rest_framework

## create django project

django-admin startproject config

## move inner forlder and manage.py outside, and remove legacy

#

- Modificações
  -- Remover status
  -- Alterar description e extra link para que sejam descopladas

- SignUp
  -- Cria Usuário
  -- Cria Company

- Login

- Criar Brag
  -- Título, duração, categoria

- Atualizar título da brag
- Atualizar duração da brag
- Atualizar categoria da brag

- Remover Brag

- Listar Brags por dia
- Listar Brags por range

- Listar estatísticas

-- Quantidade de brags
-- Categorias Principais

- Listar Categorias do Usuário
- Listar Categorias do Usuário e sua Companhia
