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