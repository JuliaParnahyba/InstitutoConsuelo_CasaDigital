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


-- ============================================
-- SEÇÃO 2 — INSERÇÃO DE DADOS (DML)
-- Objetivo: cadastrar dados mínimos para praticar consultas
-- Passos:
--  1) Inserir categorias (pai)
--  2) Inserir produtos (filho) referenciando as categorias reais
--     usando subconsultas para pegar o id correto por nome
-- ============================================

-- 1) Insere 5 categorias distintas
INSERT INTO categoria (nome)
VALUES 
    ('Eletronico'),
    ('Eletrodomestico'),
    ('Mobiliario'),
    ('Brinquedos'),
    ('Livros');

-- 2) Insere produtos vinculados às categorias existentes
--    Nota: cada subselect busca o id da categoria pelo nome
INSERT INTO produtos (categoria_id, nome, marca, modelo, n_serie, preco, estoque)
VALUES
    ((SELECT id FROM categoria WHERE nome = 'Eletronico'), 
        'Notebook Lenovo IdeaPad 3', 'Lenovo', 'IdeaPad 3', 'NB12345', 3500.00, 10),
    
    ((SELECT id FROM categoria WHERE nome = 'Eletronico'),
        'Smartphone Samsung Galaxy S20', 'Samsung', 'Galaxy S20', 'SM54321', 2500.00, 25),

    ((SELECT id FROM categoria WHERE nome = 'Eletrodomestico'),
        'Geladeira Brastemp Frost Free 375L', 'Brastemp', 'BRM44HK', 'ED001', 3200.00, 5),

    ((SELECT id FROM categoria WHERE nome = 'Mobiliario'),
        'Mesa de Jantar 4 lugares', 'Mobly', 'Mesa MDF', 'MB001', 1200.00, 8),

    ((SELECT id FROM categoria WHERE nome = 'Brinquedos'),
        'Quebra-Cabeça 500 Peças Paisagem', 'Grow', 'Puzzle500', 'BQ001', 70.00, 25),

    ((SELECT id FROM categoria WHERE nome = 'Livros'),
        'Use a Cabeça! SQL', 'Novatec', '1ª Edição', 'LV001', 120.00, 12);


-- ============================================
-- SEÇÃO 3 — CONSULTAS COM WHERE (filtros)
-- Objetivo: recuperar subconjuntos específicos de dados
-- Conceitos:
--  comparação numérica (preço > 1000)
--  combinação de condições (AND)
--  igualdade textual
-- ============================================

-- WHERE #1: filtra por marca E modelo específicos (AND)
SELECT id, nome, preco 
FROM produtos 
WHERE marca = 'Lenovo' AND modelo = 'IdeaPad 3';

-- WHERE #2: filtra por faixa de preço (maior que 1000)
SELECT id, nome, marca, modelo, preco
FROM produtos
WHERE preco > 1000;

-- WHERE #3: filtra por valor exato de texto (marca = 'Samsung')
SELECT id, nome, marca, modelo, preco
FROM produtos
WHERE marca = 'Samsung';

-- ============================================
-- SEÇÃO 4 — CONSULTA COM ORDER BY (ordenação)
-- Objetivo: classificar o resultado por uma coluna
-- Nota: DESC = do maior para o menor (aqui, prioriza itens mais caros)
-- ============================================
SELECT id, nome, marca, modelo, preco
FROM produtos
ORDER BY preco DESC;


-- ============================================
-- SEÇÃO 5 — CONSULTA COM JOIN (junção de tabelas)
-- Objetivo: combinar dados relacionados de duas tabelas
-- Conceitos:
--  alias de tabela (prod -> produtos, cat -> categoria)
--  ON cat.id = prod.categoria_id garante a correspondência
--  ORDER BY por nome da categoria e do produto para leitura
-- ============================================
SELECT
    prod.id,
    prod.nome,
    prod.marca,
    prod.modelo,
    prod.preco,
    cat.nome AS categoria
FROM produtos prod
JOIN categoria cat ON cat.id = prod.categoria_id
ORDER BY cat.nome, prod.nome;