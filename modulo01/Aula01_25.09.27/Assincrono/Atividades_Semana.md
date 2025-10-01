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
CREATE TABLE Clientes (
    ClienteID SERIAL PRIMARY KEY,

    PrimeiroNome TEXT NOT NULL,
    UltimoNome TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE TelefonesCliente (
    TelefoneID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID),

    NumTipo VARCHAR(20) NOT NULL,
    Numero VARCHAR(30) NOT NULL, -- Incluir check?
    UNIQUE (ClienteID, NumTipo, Numero)
);

CREATE TABLE EnderecosCliente (
    EnderecoID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID),

    EnderecoTipo VARCHAR (40),

    EnderecoCEP VARCHAR(10) NOT NULL,
    EnderecoLogradouro TEXT NOT NULL,
    EnderecoNumero VARCHAR(10) NOT NULL,
    EnderecoComplemento VARCHAR(30),
    EnderecoBairro VARCHAR(60) NOT NULL,
    EnderecoCidade VARCHAR(60) NOT NULL,
    EnderecoEstado CHAR(2) NOT NULL,
    EnderecoPais VARCHAR(40) NOT NULL,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE CategoriasProdutos (
    CategoriaID SERIAL PRIMARY KEY,
    NomeCategoria VARCHAR (50) UNIQUE NOT NULL,

    CreatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UpdatedAt TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE Produtos (
    ProdutoID SERIAL PRIMARY KEY,
    CategoriaID INT REFERENCES CategoriasProdutos(CategoriaID) NOT NULL,

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

CREATE TABLE DetalhesPedidosCliente ( --
    DetalhesID SERIAL PRIMARY KEY,
    PedidoID SERIAL FOREIGN KEY REFERENCES PedidosCliente(PedidoID),

    DataPedido DATE NOT NULL -- Referenciar a data do pedido

    NomeProdutoPedido VARCHAR(100) NOT NULL -- Referenciar o nome do produto
    ProdutoCategoria VARCHAR(50) NOT NULL -- Referenciar a categoria do produto
    PrecoProdutoPedido DECIMAL(10,2) NOT NULL -- Referenciar o preco pago no ato da compra

    EnderecoEntrega VARCHAR (300) -- Referenciar o endereco de entrega escolhido pelo cliente

    StatusEntrega VARCHAR(10) NOT NULL, -- Para futura informação de rastreio

    CodVendedor INT -- Referenciar o vendedor que fez o pedido (mesmo que não tenha havido nenhum)
);

CREATE TABLE PedidosCliente (
    PedidoID SERIAL PRIMARY KEY,
    ClienteID INT NOT NULL REFERENCES Clientes(ClienteID),
    DataPedido DATE NOT NULL,
)
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