# Python no Comando: Scripts que Encantam

**Objetivo da Aula**

- Modularização de código profissinalmente
- Tratar dados com segurança
- Aplicar boas práticas em Python
- Criar testes unitários
---

<br>

## Modularização

### _Por que modularizar?_
Problema |Solução 
:--------|:-------
Código difícil de manter | Colaboração eficiente
Duplicação constante | Código reutilizável
Testes impossíveis | Manutenção fácil
Bugs recorrentes | Testes isolados

<br>

_Modularização é o processo de dividir o código em partes menores, organizadas de acordo aos objetivos e ações de cada função, as quais são independentes e que poderão ser reutilizadas._

<br>

> TDD, cria primeiro o teste s desenvolve depois

<br>

## Princípio de Design

### Princípios SOLID (_simplificado_)

- 🎯 Single Responsability

    > Uma função = Uma tarefa

- DRY (Don't Repeat Yorself)

    > Não copie código, crie funções

- KISS (Keep It Simple)

    > Simples é melhor que complexo

<br>

## Anatomia de uma Função Python

```py
def processar(parametros):
    '''
    função modularizada
    '''

def nome_descritivo(parametros):
    '''
    Docstring [Comentário replicado pelo VS Code]
    '''
    """
    Docstring clara e completa [Comentário replicado pelo VS Code]
    """
    # Validações de início
    if not parametros:
        raise ValueError("...")
    
    # Logica principal
    resultado = processar(parametros)

    return resultado
```

<br>

## Comparação Visual

### Código monolítico
- Difícil de testar
- Difícil de reutilizar
- Mudanças quebram tudo

### Código Modular
- Fácil de testar
- Fácil de reutilizar
- Mais fácil de encontrar erros quando quebra e quando quebrar, não quebra tudo

    > Ainda assim, a mautenção pode ser mais difícil em códigos modulares, por estarem divididos e terem diversas bibliotecas.

<br>

```
CÓDIGO MONOLÍTICO    
[Diagrama visual:]
-----------------------
|                     |
|                     |
|     1000 linhas     |
|     tudo junto      |
|                     |
-----------------------

             VS

CÓDIGO MODULAR
[Diagrama visual:]
-------------     -------------
|   Mod.1   |     |   Mod.2   |
-------------     -------------
      |                 |
-------------------------------
|                             |
|            MAIN             |
|                             |
-------------------------------
```

## Estrutura de Projeto Profissional
```
projeto_encantador/
│
├── src/                # Código fonte principal
│   ├── models/         # Modelos/classes de dados
│   ├── utils/          # Utilitários/helpers
│   └── services/       # Lógica de negócio
|
├── tests/              # Testes unitários
├── data/               # Dados e arquivos
├── docs/               # Documentação do projeto
|
├── README.md           # Documentação geral do projeto
├── requirements.txt    # Dependências
└── .gitignore          # Arquivos a ignorar no Git
```

## Namespaces e Imports

Recomendado |Não recomendado 
:--------|:-------
`import modulo` | `from modulo import *`
`from modulo` | 
`import` | 
`funcao_especifica` | 
`import pacote.modulo as alias` |

<br>

## Escopo de Variável

```
GLOBAL
  │
  ├──
```


## Atividades

### #1 - Validador de Senhas
Criar validador com:
- Mínimo de 8 caracteres
- Letra maiúscula
- Letra minúscula
- Número
- Caractere especial

Criar 5 testes diferentes<br>

_Material completo no arquivo .md_


---

<br>

## Testes Unitários

### Por que testar?
- Economia: bugs antes da produção
- Segurança: confiança para refatorar
- Documentação: exemplos de usos vivos
- Qualidade: código melhor estruturado

**UNIDADE** = Menos parte testável

### Padrão AAA


<br>
<br>

---
### Conteúdo Extra
> Mermaid Github: [clique aqui](https://www.google.com/aclk?sa=L&pf=1&ai=DChsSEwjBmNLrn5yQAxUBVUgAHWqDH34YACICCAEQABoCY2U&co=1&ase=2&gclid=EAIaIQobChMIwZjS65-ckAMVAVVIAB1qgx9-EAAYASAAEgKTEPD_BwE&cid=CAASNuRoF7EYjca_W-9z1hWK70EEit2Kdwk9j7xZkkAazw2vQU_mVwmVYSZ1uL_3QGSt636_jEHEUw&cce=2&category=acrcp_v1_32&sig=AOD64_3pTakXEofDw2sbqviPs_pXYmUpqw&q&nis=4&adurl=https://www.mermaidchart.com/landing?utm_term%3Dmermaid%2520github%26utm_campaign%3Dmermaidecosystemfocus-G%26utm_content%3Dmermaid_broad%26utm_source%3Dgoogle_ads%26utm_medium%3Dprimary_search%26utm_term%3Dmermaid%2520github%26utm_campaign%3Dmermaidecosystemfocus-G%26utm_content%3Dmermaid_broad%26utm_source%3Dgoogle_ads%26utm_medium%3Dprimary_search%26gad_source%3D1%26gad_campaignid%3D21291684840%26gbraid%3D0AAAAAqtlhyxWgLHLKXBesR_T_g6vGVKXP%26gclid%3DEAIaIQobChMIwZjS65-ckAMVAVVIAB1qgx9-EAAYASAAEgKTEPD_BwE&ved=2ahUKEwjn4s3rn5yQAxUIFbkGHeATMNkQ0Qx6BAgMEAE)