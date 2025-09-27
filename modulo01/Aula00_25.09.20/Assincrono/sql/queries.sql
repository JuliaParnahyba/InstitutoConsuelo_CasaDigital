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