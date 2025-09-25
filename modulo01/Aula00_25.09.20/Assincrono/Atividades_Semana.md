# 🏡 Atividades Assíncronas (para casa) 

## 1. Pesquisa sobre SGBDs Pesquisar outros SGBDs além do PostgreSQL (MySQL, Oracle, SQL Server, SQLite) e escrever 1 parágrafo sobre um deles, incluindo: 
- Principais características 
- Casos de uso típicos 
- Vantagens e desvantagens 

## 2. Script SQL Prático Criar um script SQL completo com: 
- Criação de 2 tabelas relacionadas (ex: produtos e categorias)

```sql
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR (50) UNIQUE NOT NULL
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    categoria_id FOREIGN KEY,
    nome VARCHAR(50) NOT NULL,
    marca VARCHAR(50) UNIQUE,
    modelo Varchar(50) UNIQUE,
    n_serie VARCHAR(100) UNIQUE,
    preco NUMERIC(10,2) CHECK (preco >= 0) NOT  NULL,
    estoque INTEGER DEFAULT 0,
    data_cadastro DATE DEFAULT CURRENT_DATE
);
```

- Inserção de pelo menos 5 registros em cada tabela 
- 3 consultas diferentes usando WHERE 
- 1 consulta com ORDER BY 
- 1 consulta com JOIN 
- Comentários explicando cada seção 

## 3. Modelagem de Sistema Escolher um sistema simples (ex: escola, loja, hospital) e: 
- Desenhar as tabelas necessárias 
- Definir os relacionamentos 
- Justificar as escolhas de tipos de dados 
- Identificar chaves primárias e estrangeiras 

## 4. Leitura Complementar Ler o capítulo introdutório do livro *Use a Cabeça! SQL* ou artigos do W3Schools sobre SQL. 

## 5. Reflexão Crítica Escrever um texto de 1 página sobre: "Quando usar SQL/Banco de Dados vs. Planilha Excel? Quais as vantagens e limitações de cada abordagem?" 

## 6. Prática com Dataset Real Baixar um dataset público simples (CSV) e: 
- Importar para PostgreSQL 
- Criar 5 consultas diferentes 
- Documentar insights encontrados