# 🏠 Atividades Assíncronas

## Parte 01 - Exercícios livres, recaptulando a aula

1. **Normalizar** a tabela PedidosProblematicos até 3FN

```sql
CREATE TABLE PedidosProblematicos (
    PedidoID INT,                   -- Deve pertencer a uma table com dados básicos do pedido

    ClienteNome VARCHAR(100),       -- Deve pertencer a uma table "Clientes"
    ClienteEmail VARCHAR(100),      -- Deve pertencer a uma table "Clientes", talvez numa "sub-table" de contatos
    ClienteCidade VARCHAR(50),      -- Deve pertencer a uma table "Clientes", talvez numa "sub-table" de endereços
    ClienteEstado VARCHAR(2),       -- Deve pertencer a uma table "Clientes", talvez numa "sub-table" de endereços
    ClienteCEP VARCHAR(10),         -- Deve pertencer a uma table "Clientes", talvez numa "sub-table" de endereços

    ProdutoNome VARCHAR(100),       -- Deve pertencer a uma table "Produtos"
    ProdutoCategoria VARCHAR(50),   -- Deve pertencer a uma table "Categorias"
    ProdutoPreco DECIMAL(10,2),     -- Deve pertencer a uma table "Produtos"

    Quantidade INT,                 -- Deve estar inserida na table dos dados do pedido
    DataPedido DATE,                -- Deve estar inserida na table dos dados do pedido

    TelefonesContato VARCHAR(200),  -- Deve pertencer a uma table "Clientes", talvez numa "sub-table" de contatos

    NomeVendedor VARCHAR(100),      -- Deve pertencer a um table "Vendedores"
    ComissaoVendedor DECIMAL(5,2),  -- Deve pertencer a um table "Vendedores", numa "sub-table" de comissões por mês?

    EnderecoCompleto VARCHAR(300)   -- Acredito que deva ser apenas em uma view (?)
);
```

**RESPOSTA**
```sql
-- ÁREA DE CLIENTE --
CREATE TABLE Clientes (
    ClienteID SERIAL PRIMARY KEY,

    PrimeiroNome TEXT NOT NULL,
    UltimoNome TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    Email TEXT NOT NULL UNIQUE, -- Pesquisar forma de validar modelo do insert, para que confirme ser um e-mail?!

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE DocumentosCliente (
    DocumentoID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID) ON DELETE CASCADE, -- FK | "ON DELETE CASCADE", se apagar cliente, apaga documentos.

    DocTipo VARCHAR(3) NOT NULL CHECK (UPPER(DocTipo) IN ('CPF', 'RG')), -- Tipo controlado, 1 por linha
    NumDoc VARCHAR(11) NOT NULL, -- Fazer validação do tipo de documento para inputar o lenght correto

    UNIQUE (ClienteID, DocTipo), -- Garante 1 documento de cada por cliente
    UNIQUE (DocTipo, NumDoc) -- Impede que haja duplicidade de documente 

    -- Pesquisar e incluir check para length de cada documento
);

CREATE TABLE TelefonesCliente (
    TelefoneID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID) ON DELETE CASCADE, -- FK | "ON DELETE CASCADE", se apagar cliente, apaga telefones.

    NumTipo VARCHAR(20) NOT NULL CHECK (UPPER(NumTipo) IN ('CELULAR', 'RESIDENCIAL', 'COMERCIAL')), -- Tipo controlado, 1 por linha
    Numero VARCHAR(30) NOT NULL, -- para manter o padrão DDD/DDI, ou estilizar no front?

    UNIQUE (ClienteID, NumTipo, Numero) -- evita duplicar o mesmo número/tipo no cliente

    -- Pesquisar e incluir check para o número de telefone
);

CREATE TABLE TiposEndereco (
    Tipo VARCHAR(20) PRIMARY KEY -- flexibilização para os tipos de endereços. O próprio usuário descreve?!
);

CREATE TABLE EnderecosCliente (
    EnderecoID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID) ON DELETE CASCADE, -- FK | "ON DELETE CASCADE", se apagar cliente, apaga telefones.

    EnderecoTipo VARCHAR(40) NOT NULL REFERENCES TiposEndereco(Tipo), -- FK | apanha o tipo na tabela de referência

    EnderecoCEP VARCHAR(10) NOT NULL,
    EnderecoLogradouro TEXT NOT NULL,
    EnderecoNumero VARCHAR(10) NOT NULL,
    EnderecoComplemento VARCHAR(30),
    EnderecoBairro VARCHAR(60) NOT NULL,
    EnderecoCidade VARCHAR(60) NOT NULL,
    EnderecoEstado CHAR(2) NOT NULL,
    EnderecoPais VARCHAR(40) NOT NULL,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ÁREA LOJAS --
CREATE TABLE LojasFisicas (
    LojaID SERIAL PRIMARY KEY,

    NomeFantasia TEXT NOT NULL,
    RazaoSocial TEXT NOT NULL,
    CNPJ VARCHAR(14) NOT NULL UNIQUE, -- validação futura com CHECK (14 dígitos)
    EmailContato TEXT,
    TelefoneContato VARCHAR(30),

    EnderecoID INT REFERENCES EnderecosCliente(EnderecoID), -- FK: podemos usar o mesmo modelo de endereços
    Ativa BOOLEAN NOT NULL DEFAULT TRUE,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE TelefonesLoja (
    TelefoneID SERIAL PRIMARY KEY,
    LojaID INT NOT NULL REFERENCES LojasFisicas(LojaID) ON DELETE CASCADE, -- FK | "ON DELETE CASCADE", se apagar loja, apaga telefonesLoja.

    Numero VARCHAR(30) NOT NULL, -- para manter o padrão DDD/DDI, ou estilizar no front?

    UNIQUE (LojaID, Numero) -- evita duplicar o mesmo número/tipo na loja

    -- Pesquisar e incluir check para o número de telefone
);

-- ÁREA VENDEDORES --
CREATE TABLE Vendedores (
    VendedorID SERIAL PRIMARY KEY,
    LojaID INT REFERENCES LojasFisicas(LojaID), -- Para indicar onde o vendedor está lotado e se é apenas vendedor online

    Nome TEXT NOT NULL,
    Sobrenome TEXT NOT NULL,
    DataNascimento DATE NOT NULL,

    Email TEXT NOT NULL UNIQUE,
    Ativo BOOLEAN NOT NULL DEFAULT TRUE, -- se profissional ainda pertence à empresa
    Cargo VARCHAR(20) NOT NULL CHECK (UPPER(Cargo) IN ('ASSISTENTE', 'SUPERVISOR', 'GERENTE')), -- cargo com lista

    CodVendedor VARCHAR(9) NOT NULL UNIQUE, -- cód do vendedor, pode ser matrícula que será usada para compras online

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE VendedoresLoja (
    VendedorID INT NOT NULL REFERENCES Vendedores(VendedorID),
    LojaID INT NOT NULL REFERENCES LojasFisicas(LojaID),

    DataInicio DATE NOT NULL,
    DataFim DATE,

    PRIMARY KEY (VendedorID, LojaID, DataInicio)
);

CREATE TABLE ComissoesVendedor (
    VendedorID INT NOT NULL REFERENCES Vendedores(VendedorID), -- FK
    PedidoID INT NOT NULL REFERENCES PedidosCliente(PedidoID), -- FK

    ValorPedido DECIMAL (10,2) NOT NULL CHECK (ValorPedido >= 0), -- Valor do pedido 
    PercentualAplicado DECIMAL(5,2) NOT NULL CHECK (PercentualAplicado >= 0), -- indicação do percentual de comissão aplicado
    ValorComissao DECIMAL (10,2) NOT NULL CHECK (ValorComissao >= 0), -- valor da comissão já calculado

    TipoVenda VARCHAR(6) NOT NULL CHECK (UPPER(TipoVenda) IN ('LOJA', 'ONLINE')), -- rastreio do canal de venda

    RegistradoEm TIMESTAMPTZ NOT NULL DEFAULT NOW(), -- para acompanhamento de quando foi efetivado o registro da comissão (casos de devolução online)
    
    PRIMARY KEY (VendedorID, PedidoID) -- chave composta, 1 linha por vendedor<>pedido
);

-- ÁREA DE PRODUTOS --
CREATE TABLE CategoriasProdutos (
    CategoriaID SERIAL PRIMARY KEY,
    NomeCategoria VARCHAR (50) UNIQUE NOT NULL,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE Produtos (
    ProdutoID SERIAL PRIMARY KEY,
    CategoriaID INT REFERENCES CategoriasProdutos(CategoriaID) NOT NULL, -- FK, obrigatória

    Nome VARCHAR(50) NOT NULL,
    Marca VARCHAR(50) NOT NULL,
    Modelo VARCHAR(50) NOT NULL,
    UNIQUE (Marca, Modelo),
    
    NumSerie VARCHAR(100) UNIQUE,
    
    PrecoAtual NUMERIC(10,2) CHECK (PrecoAtual >= 0) NOT NULL,
    
    Estoque INTEGER CHECK (Estoque >= 0) DEFAULT 0,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ÁREA DE PEDIDOS --
CREATE TABLE PedidosCliente (
    PedidoID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID), -- FK
    EnderecoEntregaID INT NOT NULL REFERENCES EnderecosCliente(EnderecoID), -- FK
    
    VendedorID INT REFERENCES Vendedores(VendedorID) ON DELETE SET NULL, -- FK | permite inativar vendedor
    
    DataPedido DATE NOT NULL,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE ItensPedido (
    PedidoID INT NOT NULL REFERENCES PedidosCliente(PedidoID) ON DELETE CASCADE, -- FK | apaga pedido, apaga itens do pedido
    ProdutoID INT NOT NULL REFERENCES Produtos(ProdutoID),
    Quantidade INT NOT NULL CHECK (Quantidade > 0),
    PrecoUnitario DECIMAL(10,2) NOT NULL, -- Um "snapshot" do preço atual, pago pelo cliente. 
    PRIMARY KEY (PedidoID, ProdutoID)
);
```

2. **Criar um modelo desnormalizado da tabela do exercício 1** para relatórios e justifique quando usar

3. **Ler capítulo sobre Views** no PostgreSQL Docs

## 📘 Lista de Exercícios – SQL com Dataset `juliaostore.sql`

## 📌 Parte 1 – Consultas Básicas
1. **Liste todos os clientes cadastrados.**
   💡 *Dica: SELECT simples na tabela Clientes*

2. **Liste todos os produtos da categoria "Acessórios".**
   💡 *Dica: WHERE com filtro de categoria*

3. **Mostre todos os pedidos feitos por Ana Silva.**
   💡 *Dica: JOIN entre Clientes e Pedidos + filtro no nome*

---

## 📌 Parte 2 – Consultas Intermediárias

4. **Exiba o valor total de cada pedido.**
   💡 *Dica: Preciso multiplicar quantidade × preço, depois somar por pedido*
   🤔 *Quais tabelas conectar? Pedidos → ItensPedido → Produtos*

5. **Traga o total gasto por cada cliente.**
   💡 *Dica: Expandir a consulta anterior agrupando por cliente*

6. **Mostre os produtos mais vendidos em quantidade.**
   💡 *Dica: SUM(Quantidade) GROUP BY Produto + ORDER BY DESC*

---

## 📌 Parte 3 – Consultas Avançadas

7. **Liste os clientes que já compraram mais de um tipo diferente de produto.**
   💡 *Dica: COUNT(DISTINCT ProdutoID) > 1*

8. **Mostre os pedidos cujo valor total foi acima de R$ 3000.**
   💡 *Dica: Use a consulta do exercício 4 + HAVING*

9. **Calcule o ticket médio dos clientes (média de valor gasto por pedido).**
   💡 *Dica: AVG() da soma dos subtotais*

10. **Liste os clientes que nunca fizeram pedidos.**
    💡 *Dica: LEFT JOIN + WHERE campo IS NULL*

---

## 🎯 Desafios Extras (Para os Ninjas!)

11. **Qual produto gerou mais receita total?**
12. **Quantos clientes compraram em setembro de 2025?**
13. **Qual a diferença entre o maior e menor ticket de pedido?**