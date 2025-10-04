# InstitutoConsuelo_CasaDigital
Repositório dedicado ao registro das aulas durante o Curso oferecido pelo Instituto Consuelo e Casa Digital.

## Aulas — Formação Fullstack Consuelo
*Organização por módulos.*

<br>

### Índice
- [modulo01](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo01) — Banco de Dados Relacinal (PostgreSQL)
    - [Aula00_25.09.20](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo01/Aula00_25.09.20) — ⚖️ Consultando com Classe: Primeiros Passos no SQL
    - [Aula01_25.09.27](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo01/Aula01_25.09.27) — 🔬 Modelagem Ninja: Esquemas que Contam Histórias
- [modulo02](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo02) — Python
    - [Aula02_25.10.04](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo02/Aula02_25.10.04) — 🍳 Python na Cozinha: Preparando os Dados
    - [Aula03_25.10.11](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo02/Aula03_25.10.11) — 🐍 Python no Comando: Scripts que Encantam
- [module03](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo03) — API
    - [Aula04_25.10.18](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo03/Aula04_25.10.18) — 🌍 Missão API: Da Teoria à Prática
    - [Aula05_25.10.26](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo03/Aula05_25.10.26) — ✨ Automatiza que Cresce: Projetos Vivos
- [modulo04](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo04) — Web (HTML/CSS/JS + integração)
    - [Aula06_25.11.01](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo04/Aula06_25.11.01) — 🌐 Front Descomplicado: HTML & CSS
    - [Aula07_25.11.08](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo04/Aula07_25.11.08) — ⚡ Conectando Mundos: JavaScript e APIs
- [module05](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo05) — Planejamento e squad
    - [Aula08_25.11.22](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo05/Aula08_25.11.22) — 🚀 Mão na Massa: Planejamento em Squad
    - [Aula09_25.11.29](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo05/Aula09_25.11.29) — 🔧 Projeto em Ação: Do Código ao Produto
    - [Aula10_25.12.13](https://github.com/JuliaParnahyba/InstitutoConsuelo_CasaDigital/tree/main/modulo05/Aula10_25.12.13) — ✨ Lapidação Final: Preparando para o Show

<br>

---

### Instruções de Execução e Testes

- **Modulo01**
    1. **Subir o Postgres com Docker**
        ```bash
        docker compose up -d
        ```

    <br>

    2. **Acessar o Container**
        ```bash
        docker exec -it aulas_db bash
        psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
        ```

        _Para confirma que os scripts estão montados:_
        ```sql
        \! ls -la /sql
        ```

    <br>
    
    3. **Executar os scripts SQL**
        ```sql
        \i /sql00/file.sql; -- aula00
        \i /sql01/file.sql; -- aula01
        ```

    <br>

    4. **Consultar tabelas e views**
        - Listar tabelas
        ```sql
        \dt
        ```
        - Listar views
        ```sql
        \dv
        ```

<br>

- **Modulo02**

    _[Ainda a ser adicionado]_

<br>

- **Modulo03**

    _[Ainda a ser adicionado]_

<br>

- **Modulo04**

    _[Ainda a ser adicionado]_

<br>

- **Modulo05**

    _[Ainda a ser adicionado]_