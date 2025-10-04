-- Views para relatórios
-- Relatório de Pedidos Simples
CREATE OR REPLACE VIEW RelatorioPedidos_Simples AS
SELECT
    p.PedidoID,
    p.DataPedido,
    (c.PrimeiroNome || ' ' || c.UltimoNome) AS ClienteNomeCompleto,
    e.EnderecoCidade AS ClienteCidade,
    e.EnderecoEstado AS ClienteEstado,
    pr.Nome AS ProdutoNome,
    pr.Marca AS ProdutoMarca,
    ip.Quantidade,
    ip.PrecoUnitario,
    (ip.Quantidade * ip.PrecoUnitario) AS ValorTotal
FROM PedidosCliente p
JOIN Clientes c ON c.ClienteID = p.ClienteID
JOIN EnderecosCliente e ON e.EnderecoID = p.EnderecoEntregaID
JOIN ItensPedido ip ON ip.PedidoID = p.PedidoID
JOIN Produtos pr ON pr.ProdutoID = ip.ProdutoID;

-- Relatório de Comissões de Vendedores por Produto
CREATE OR REPLACE VIEW RelatorioComissaoVendedores_Produto AS
SELECT
    cv.VendedorID,
    (v.Nome || ' ' || v.Sobrenome) AS VendedorNomeCompleto,
    cv.PedidoID,
    p.DataPedido,

    pr.ProdutoID,
    pr.Nome AS ProdutoNome,
    pr.Marca AS ProdutoMarca,
    
    ip.Quantidade,
    ip.PrecoUnitario,
    (ip.Quantidade * ip.PrecoUnitario) AS ValorLinha,
    
    cv.TipoVenda,
    cv.PercentualAplicado,
    cv.ValorPedido,
    cv.ValorComissao
FROM ComissoesVendedor cv
JOIN Vendedores v ON v.VendedorID = cv.VendedorID
JOIN PedidosCliente p ON p.PedidoID = cv.PedidoID
JOIN ItensPedido ip ON ip.PedidoID = cv.PedidoID
JOIN Produtos pr ON pr.ProdutoID = ip.ProdutoID;

-- Relatório de Comissões de Vendedores por pedido
CREATE OR REPLACE VIEW RelatorioComissaoVendedores_Pedido AS
SELECT
    cv.VendedorID,
    (v.Nome || ' ' || v.Sobrenome) AS VendedorNomeCompleto,
    cv.PedidoID,
    p.DataPedido,
    cv.TipoVenda,
    cv.PercentualAplicado,
    cv.ValorPedido,
    cv.ValorComissao
FROM ComissoesVendedor cv
JOIN Vendedores v ON v.VendedorID = cv.VendedorID
JOIN PedidosCliente p ON p.PedidoID = cv.PedidoID;