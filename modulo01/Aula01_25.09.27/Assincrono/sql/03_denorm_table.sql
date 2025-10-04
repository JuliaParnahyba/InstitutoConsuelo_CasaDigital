BEGIN;

DROP TABLE IF EXISTS RelatorioPedidos_Denorm;

CREATE TABLE RelatorioPedidos_Denorm (
    PedidoID INT NOT NULL,
    ProdutoID INT NOT NULL,
    DataPedido DATE NOT NULL,
    
    ClienteID INT NOT NULL,
    ClienteNome TEXT NOT NULL,
    ClienteSobrenome TEXT NOT NULL,
    ClienteCidade TEXT NOT NULL,
    ClienteEstado CHAR(2) NOT NULL,

    ProdutoNome VARCHAR(50) NOT NULL,
    ProdutoMarca VARCHAR(50) NOT NULL,
    CategoriaProduto VARCHAR(50) NOT NULL,

    Quantidade INT NOT NULL,
    PrecoUnitario DECIMAL(10,2) NOT NULL,
    ValorTotal DECIMAL(10,2) NOT NULL,

    VendedorID INT,
    NomeVendedor TEXT,

    VendaTipo VARCHAR(10),
    LocalVendedor TEXT,
    ComissaoVendedor DECIMAL(10,2),
    ValorPedido DECIMAL(10,2),
    ValorComissao DECIMAL(10,2),

    PRIMARY KEY (PedidoID, ProdutoID)
);

COMMIT;