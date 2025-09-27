-- ============================================
-- SEÇÃO 1 — CRIAÇÃO DE 2 TABELAS RELACIONADAS
-- Objetivo: definir estrutura (DDL) e integridade básica
--  categoria: tabela “pai” (lista controlada de categorias)
--  produtos:  tabela “filha” que referencia categoria via FK
-- ============================================

-- Tabela PAI: guarda nomes únicos de categorias.
-- Decisões:
--  id SERIAL PRIMARY KEY: identificador numérico simples e auto-incrementado
--  nome UNIQUE NOT NULL: impede categorias duplicadas e exige preenchimento
--  created_at / updated_at: registro de quando foi criado/alterado (a definir trigger)
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR (50) UNIQUE NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Tabela FILHA: cada produto pertence a 1 categoria (chave estrangeira).
-- Decisões:
--  categoria_id REFERENCES categoria(id) NOT NULL: obriga vínculo com categoria existente
--  UNIQUE (marca, modelo): evita duplicatas semânticas (mesmo item cadastrado duas vezes)
--  n_serie UNIQUE: número de série não pode repetir (se informado)
--  preco NUMERIC(10,2) + CHECK >= 0: precisão para financeiro e validação de não-negativo
--  estoque INTEGER DEFAULT 0 + CHECK >= 0: inicia em 0 e não permite negativo
--  created_at / updated_at: registro temporal (atualização manual quando fizer UPDATE)
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    categoria_id INT REFERENCES categoria(id) NOT NULL,

    nome VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    UNIQUE (marca, modelo), 
    
    n_serie VARCHAR(100) UNIQUE,
    
    preco NUMERIC(10,2) CHECK (preco >= 0) NOT NULL,
    
    estoque INTEGER CHECK (estoque >= 0) DEFAULT 0,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
