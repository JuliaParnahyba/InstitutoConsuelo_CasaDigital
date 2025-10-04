BEGIN;

-- Limpeza para reexecução durante os estudos
TRUNCATE
  ComissoesVendedor,
  ItensPedido,
  PedidosCliente,
  Produtos,
  CategoriasProdutos,
  VendedoresLoja,
  Vendedores,
  TelefonesLoja,
  LojasFisicas,
  EnderecosCliente,
  TiposEndereco,
  TelefonesCliente,
  DocumentosCliente,
  Clientes
RESTART IDENTITY CASCADE;

-- Inserir dados na tabela de Clientes
INSERT INTO Clientes (PrimeiroNome, UltimoNome, DataNascimento, Email) VALUES
('João', 'Silva', '1985-06-15', 'joao.silva@example.com'),
('Maria', 'Oliveira', '1990-09-22', 'maria.oliveira@example.com'),
('Carlos', 'Santos', '1978-12-05', 'carlos.santos@example.com');

-- Inserir dados na tabela de DocumentosCliente
INSERT INTO DocumentosCliente (ClienteID, DocTipo, NumDoc) VALUES
(1, 'CPF', '12345678901'),
(1, 'RG', '123456789'),
(2, 'CPF', '98765432100'),
(2, 'RG', '765432101'),
(3, 'CPF', '45678912300'),
(3, 'RG', '456123789');

-- Inserir dados na tabela de TelefonesCliente
INSERT INTO TelefonesCliente (ClienteID, NumTipo, Numero) VALUES
(1, 'CELULAR', '+5511999999999'),
(1, 'RESIDENCIAL', '+551133333333'),
(2, 'CELULAR', '+5511888888888'),
(2, 'COMERCIAL', '+551122222222'),
(3, 'CELULAR', '+5511777777777');

-- Inserir dados na tabela de TiposEndereco
INSERT INTO TiposEndereco (Tipo) VALUES
('RESIDENCIAL'),
('COMERCIAL'),
('ENTREGA'),
('COBRANCA');

-- Inserir dados na tabela de EnderecosCliente
INSERT INTO EnderecosCliente (ClienteID, EnderecoTipo, EnderecoCEP, EnderecoLogradouro, EnderecoNumero, EnderecoComplemento, EnderecoBairro, EnderecoCidade, EnderecoEstado, EnderecoPais) VALUES
(1, 'RESIDENCIAL', '01001-000', 'Rua A', '100', 'Apto 101', 'Centro', 'São Paulo', 'SP', 'Brasil'),
(1, 'ENTREGA', '01002-000', 'Avenida B', '200', NULL, 'Jardins', 'São Paulo', 'SP', 'Brasil'),
(2, 'COBRANCA', '02001-000', 'Rua C', '300', 'Casa', 'Vila Mariana', 'São Paulo', 'SP', 'Brasil'),
(2, 'ENTREGA', '02002-000', 'Avenida C', '300', NULL, 'Vila Mariana', 'São Paulo', 'SP', 'Brasil'),
(3, 'ENTREGA', '03001-000', 'Avenida D', '400', NULL, 'Moema', 'São Paulo', 'SP', 'Brasil');

-- Inserir dados na tabela de LojasFisicas
INSERT INTO LojasFisicas (NomeFantasia, RazaoSocial, CNPJ, EmailContato, TelefoneContato, EnderecoID, Ativa) VALUES
('Loja Central', 'Loja Central Ltda', '12345678000199', 'contato@lojacentral.com.br', '+5511999999999', 1, TRUE),
('Loja Norte', 'Loja Norte Ltda', '98765432000188', 'contato@lojanorte.com.br', '+5511988888888', 2, TRUE),
('Loja Sul', 'Loja Sul Ltda', '45678912000177', 'contato@lojasul.com.br', '+5511777777777', 3, TRUE);

-- Inserir dados na tabela de TelefonesLoja
INSERT INTO TelefonesLoja (LojaID, Numero) VALUES
(1, '+5511999999999'),
(2, '+5511988888888'),
(3, '+5511777777777');

-- Inserir dados na tabela de Vendedores
INSERT INTO Vendedores (LojaID, Nome, Sobrenome, DataNascimento, Email, Ativo, Cargo, CodVendedor) VALUES
(1, 'Ana', 'Pereira', '1985-06-15', 'ana.pereira@example.com', TRUE, 'ASSISTENTE', 'V001'),
(1, 'Daniel', 'Almeida', '1982-03-10', 'daniel.almeida@example.com', TRUE, 'GERENTE', 'V004'),
(2, 'Bruno', 'Costa', '1990-09-22', 'bruno.costa@example.com', TRUE, 'ASSISTENTE', 'V002'),
(3, 'Carla', 'Rocha', '1978-12-05', 'carla.rocha@example.com', TRUE, 'GERENTE', 'V003'),
(3, 'Eduardo', 'Mendes', '1988-11-30', 'eduardo.mendes@example.com', TRUE, 'ASSISTENTE', 'V005');

-- Inserir dados na tabela de VendedoresLoja
INSERT INTO VendedoresLoja (VendedorID, LojaID, DataInicio, DataFim) VALUES
(1, 1, '2023-01-01', NULL),
(2, 1, '2023-01-01', NULL),
(3, 2, '2023-01-01', NULL),
(4, 3, '2023-01-01', NULL),
(5, 3, '2023-01-01', NULL);

-- Inserir dados na tabela de CategoriasProdutos
INSERT INTO CategoriasProdutos (NomeCategoria) VALUES
('Eletrônicos'),
('Roupas'),
('Calçados'),
('Livros'),
('Móveis');

-- Inserir dados na tabela de Produtos
INSERT INTO Produtos (CategoriaID, Nome, Marca, Modelo, NumSerie, PrecoAtual, Estoque) VALUES
(1, 'TV 55"', 'Samsung', 'QLED55', 'SN-TV-001', 3500.00, 12),
(2, 'Notebook 14"', 'Dell', 'Inspiron14', 'SN-NB-001', 4200.00, 8),
(3, 'Smartphone', 'Apple', 'iPhone 13', 'SN-PH-001', 5200.00, 5),
(2, 'Mouse', 'Logitech', 'M280', 'SN-MS-001', 120.00, 50);

-- Inserir dados na tabela de PedidosCliente
INSERT INTO PedidosCliente (ClienteID, EnderecoEntregaID, VendedorID, DataPedido) VALUES
(1, 2, 1, '2023-10-01'),
(2, 4, 3, '2023-10-02'),
(3, 5, 4, '2023-10-03');

-- Inserir dados na tabela de ItensPedido
INSERT INTO ItensPedido (PedidoID, ProdutoID, Quantidade, PrecoUnitario) VALUES
(1, 1, 1, 3500.00),
(1, 4, 2, 120.00),
(2, 2, 1, 4200.00),
(3, 3, 1, 5200.00); 

-- Calculando e inserindo comissões na tabela de ComissoesVendedor
INSERT INTO ComissoesVendedor (VendedorID, PedidoID, ValorPedido, PercentualAplicado, ValorComissao, TipoVenda)
SELECT 
       p.VendedorID, p.PedidoID, 
       SUM(ip.Quantidade * ip.PrecoUnitario) AS ValorPedido,
       3.00 AS PercentualAplicado,
       SUM(ip.Quantidade * ip.PrecoUnitario) * 0.03 AS ValorComissao,
       'LOJA'::VARCHAR(6)
FROM PedidosCliente p
JOIN ItensPedido ip ON ip.PedidoID = p.PedidoID
WHERE p.PedidoID IN (1,3)
GROUP BY p.VendedorID, p.PedidoID;

INSERT INTO ComissoesVendedor (VendedorID, PedidoID, ValorPedido, PercentualAplicado, ValorComissao, TipoVenda)
SELECT 
       p.VendedorID, p.PedidoID, 
       SUM(ip.Quantidade * ip.PrecoUnitario) AS ValorPedido,
       2.50 AS PercentualAplicado,
       SUM(ip.Quantidade * ip.PrecoUnitario) * 0.025 AS ValorComissao,
       'ONLINE'::VARCHAR(6)
FROM PedidosCliente p
JOIN ItensPedido ip ON ip.PedidoID = p.PedidoID
WHERE p.PedidoID = 2
GROUP BY p.VendedorID, p.PedidoID;

COMMIT;
