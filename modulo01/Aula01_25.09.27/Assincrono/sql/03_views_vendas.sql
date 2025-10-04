-- Relatório de região com mais pedidos
CREATE OR REPLACE VIEW RelatorioRegiao_MaisPedidos AS
SELECT
    e.EnderecoEstado AS Estado,
    e.EnderecoCidade AS Cidade,

    COUNT(DISTINCT p.PedidoID) AS NumPedidos,
    SUM(ip.Quantidade) AS ItensVendidos,
    SUM(ip.Quantidade * ip.PrecoUnitario)::numeric AS Faturamento
FROM PedidosCliente p
JOIN EnderecosCliente e ON e.EnderecoID = p.EnderecoEntregaID
JOIN ItensPedido ip ON ip.PedidoID = p.PedidoID
GROUP BY e.EnderecoEstado, e.EnderecoCidade
ORDER BY NumPedidos DESC, ItensVendidos DESC;

-- Relatório de produtos mais vendidos
CREATE OR REPLACE VIEW RelatorioProdutos_MaisVendidos AS
SELECT
    pr.ProdutoID,
    pr.Nome AS ProdutoNome,
    pr.Marca AS ProdutoMarca,
    cat.NomeCategoria AS CategoriaProduto,

    SUM(ip.Quantidade) AS QtdeVendida,
    SUM(ip.Quantidade * ip.PrecoUnitario)::numeric AS Faturamento,
    (SUM(ip.Quantidade * ip.PrecoUnitario) / NULLIF(SUM(ip.Quantidade), 0))::numeric(10,2) AS PrecoMedioPonderado
FROM ItensPedido ip
JOIN Produtos pr ON pr.ProdutoID = ip.ProdutoID
JOIN CategoriasProdutos cat ON cat.CategoriaID = pr.CategoriaID
GROUP BY pr.ProdutoID, pr.Nome, pr.Marca, cat.NomeCategoria
ORDER BY QtdeVendida DESC;