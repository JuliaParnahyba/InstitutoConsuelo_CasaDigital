# Modelagem Ninja | Esquemas que Contam História

**O que está errado?**
```sql
CREATE TABLE Pedidos (
    pedido_id INT, -- Sem serial e indicação de chaev primária
    cliente_nome VARCHAR(100), -- Ideial seria dividir entre nome e sobrenome, não referencia uma tabela de clientes
    produtos_comprados VARCHAR(500), -- Múltiplos valores e não referencia a tabela de produtos, por exemplo
    telefones VARCHAR (200), -- Múltiplos valores e pode se tornar confuso
    vendedor_nome VARCHAR(100), -- Segue a mesma lógica do cliente_nome, depende do produto
    comissao DECIMAL(5,2) -- Depende do vendedor
)
```

## Normalização de Dados
Processo de estruturação das tables para reduzir redundâncis e inconsistência, possibilitando integridade dos dados, consistência e clareza no modelo. Porém pode gerar consultas mais complexas.

Ao normalizar, significa dizer que iremos trazer os dados para uma norma, isto é, aquilo que dita as boas práticas e que podem ser investigadas em livros.

**Níveis**: São 10 níveis de regra, dos quais veremos 3 regras.

<br>

### Primeira Forma Normal (1FN)
> Cada célula = **UM** valor atômico <br>
> cada atributo pode ter apenas um valor por registro.

<br>

Dificilmente haverá uma linha no plural, se houver necessidade de colocar no plural, significa que deverá ser criada uma table para tal.


```sql
-- Viola 1FN
CREATE TABLE ClientesRuim (
    ClienteID INT,
    Nome VARCHAR(100),
    Telefones VARCHAR(200) -- "11999999999;1188888888;11777777777"  
);
```

```sql
-- Atende 1FN
CREATE TABLE Clientes (
    ClienteID INT,
    Nome VARCHAR(100),
    PRIMARY KEY (ClienteID)
);

CREATE TABLE TelefoneCliente(
    TelefoneID INT PRIMARY KEY,
    ClienteID INT,
    Telefone VARCHAR(20),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(clienteID)
);
```

<br>

### Segunda Forma Normal (2FN)
É quando está adequada à 1FN e todos os atributos não chave primária puderem ser obtidos da combinação de todos os atributos que formam a chave primária. 

```sql
-- Viola 2FN - NomeAluno depende só de AlunoID, não da chave completa
CREATE TABLE MatriculaRuim (
    AlunoID INT,
    CursoID INT,
    NomeAluno VARCHAR-- Depende só de Aluno
    NotaFiscal DECIMAL(4,2), -- Depende da chave completa (AlunoID + CursoID),
    PRIMARY KEY (AlunoID, CursoID)
);
```

```sql
-- Atende 2FN
CREATE TABLE Alunos (
    AlunosID INT PRIMARY KEY,
    Nome VARCHAR(100)
);

CREATE TABLE Matriculas (
    AlunoID INT,
    CursoID INT,
    NotaFiscal DECIMAL(4,2),
    PRIMARY KEY (AlunoID, CursoID),
    FOREIGN KEY (AlunoID) REFERENCES Alunos(AlunoID)
);
```

<br>

### Terceira
1FN + 2FN mas sem dependências transitivas

```sql
-- Viola 3FN - DepartamentoNome depende de DepartamentoID, não do funcionário
CREATE TABLE FuncionarioRuim (
    FuncionarioID INT PRIMARY KEY,
    Nome VARCHAR(100),
    DepartamentoID INT,
    DepartamentoNome VARCHAR(100) -- Dependência transitiva (transita entre funcionários)!
);

-- DepartamentoNome depende de DepartamentoID
-- Não do FuncionárioID diretamente
```

```sql
-- Atende 3FN
CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY,
    Nome VARCHAR(100)
);

CREATE TABLE Funcionarios (
    FuncionarioID INT PRIMARY KEY,
    Nome VARCHAR(100),
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
);
```

<br>

## Atividade
Identificar problemas na tabela a seguir, classificando qual FN está sendo impactada.

```sql
CREATE TABLE PedidosProblematicos (
    PedidoID INT,
    ClienteNome VARCHAR(100),
    ClienteEmail VARCHAR(100),
    Quantidade INT,
    DataPedido DATE,
    NomeVendedor VARCHAR(100),

    -- ClienteCidedade, ClienteEstado, ClienteCEP, dependem de ClienteID ou do endereço do cliente
    ClienteCidade VARCHAR(50), -- REGRA 3FN
    ClienteEstado VARCHAR(2), -- REGRA 3FN
    ClienteCEP VARCHAR(10), -- REGRA 3FN

    ProdutoNome VARCHAR(100), 
    -- ProdutoCategoria e PrecoProduto depende de ProdutoNome, se é sabido o produto, sabe-se também a categoria e preço
    ProdutoCategoria VARCHAR(50), -- REGRA 3FN
    ProdutoPreco DECIMAL(10,2), -- RERA 3FN
 
    -- TelefonesContato pode guardar vários telefones e EnderecoCompleto, guarda excesso de informação
    TelefonesContato VARCHAR(200), -- REGRA 1FN
    EnderecoCompleto VARCHAR(300) -- REGRA 1FN

    -- ComissaoVendedor depende apenas do vendedor, não do pedido completo
    ComissaoVendedor DECIMAL(5,2), -- REGRA 2FN 
)
```

```sql
-- normalizar o exemplo acima
```

<br>

## Desnormalização (VIEW)
Propositadamente é induzida a redundância para melhorar performance, sendo usana em cenários de relatórios, análises ráidas, data warehouses etc..

### Normalização vs Desnormalização

#### Normalizarção
- Dados íntegros
- Sem redundância
- Atualizações fáceis

#### Desnormalização
- Consultas rápidas
- Relatórios simples
- Menos JOINs
- Dados duplicados

<br>

> Para desnormalizar usa-se uma VIEW, que de forma simples é uma cópia de uma tabela, que fica em memória, facilitando e "barateando" consultas, queries.

<br>

Uma view pode ser da maneira que for desejada, uma vez que é uma visualização, ela deverá atender às necessidades para agilidade de consulta entre outras necessidades.

```sql
-- Tabela normalizada (ideal para transações)
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    DataPedido DATE
);

-- Tabela desnormalizada (ideal para relatórios)
CREATE TABLE RelatorioVendasMensal (
    Mes VARCHAR(7),
    ClienteNome VARCHAR(100),
    QtdePedidos INT,
    TocketMedio DECIMAL(10,2)
);
```

#### Caso prático

- 50.000 alunos
- 1.000 cursos
- Relatórios de notas todo semestre
- Matrículas mudam todo semestre

<br>

> <br>
>
> **Construção**
> <br> 
> - *Tabela de alunos* <br>
> - *Tabela de cursos* - associado às matérias que, por sua vez, estará associada aos relatórios de notas por semestre. <br>
> - *Tabela de semestre* - que recebe os alunos com seus respectivos cursos, matérias e notas. <br>
> As matrículas podem ser geradas via script a cada inscrição semestral, que será armazenada no aluno. <br><br>

<br>

**Dicas de ouro:**
- Projete sempre normalizado primeiro
- Desnormalize apenas onde necessário
- Use VIEWS para simular desnormalização
- Meça e performance antes de decidir

<br>

> <br>
> 
> ***Otimização prematura é raiz de todo mal"***
> <br><br>


## Atividade: Análise de Melhorias

Com base no esquema de E-COMMERCE, o que poderia ser melhor?

**4 tabelas principais:
- Cliente (dados)


<br>
<br>

---

Estudar UML

[Pagina de cursos para Web - Informática para Internet](https://materialpublic.imd.ufrn.br/curso/disciplina/3)

[Site Metrópole Digital "Material Didático"](https://materialpublic.imd.ufrn.br/curso/disciplina/3/73), onde há conteúdos de BD.

---