# Missão Frontend Interativo: JavaScript e Integração com APIs

## Mod. III - DOM: Seleção de Modificação de Eventos
DOM [**D**ocument **O**bject **M**odel] - Árvore de objetos de toda a estrutura HTML que o JS pode manipular

**E** → Elemento | **I** → Interação | **R** → Resultado desejado

> _Componentes de React é basicamente uma tag salva dentro de uma variável_

<br>

### Exemplo
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Minha Página</title>
  </head>
  <body>
    <h1>Título</h1>
    <p>Parágrafo</p>
  </body>
</html>
```

```bash
Árvore DOM:
document
  └── html
      ├── head
      │   └── title
      │       └── "Minha Página"
      └── body
          ├── h1
          │   └── "Título"
          └── p
              └── "Parágrafo"
```

### Manipulação do DOM
...

<br>

## Módulo IV - Arrays Objetos e Seus Métodos
_Array é um objeto especial para armazenar múltiplos valores em uma única variável_

```js
const numeros = [1, 2, 3, 4, 5];
```

<br>

### Arrays: Métodos Essenciais
1. Map: método que transforma cada item do array original em um novo item
    ```js
    const numeros = [1, 2, 3, 4, 5];

    const dobrados = numeros.map(n => n * 2);
    // [2, 4, 6, 8, 10]
    ```

2. Filter: quer filtrar a partir de uma condição, capturando aqueles que a condição for verdadeira
    ```js
    const numeros = [1, 2, 3, 4, 5];

    const pares = numeros.filter(n => n % 2 === 0);
    // [2, 4]
    ```

3. Find: busca o primeiro que saisfizer a condiçãp
    ```js
    const numeros = [1, 2, 3, 4, 5];

    const maior2 = numeros.find(n => n > 3);
    // 4
    ```

4. Reduce: acumula valor
    ```js
    const numeros = [1, 2, 3, 4, 5];

    const soma = numeros.reduce((acc, n) => acc + n, 0);
    // 
    ```

<br>

### Objetos
```js
// Criação
const usuario = {
    nome: 'Joao da Silva',
    idade: 30,
    email: 'joaodasilva@gmail.com',
    ativo: true
}

// Acessar propriedades
console.log(usuario.nome);      //dot notation
console.log(usuario['email']);  // bracket notation

// adicionando/modificando
usuario.telefone = '123456789';
usuario.idade = 31;

// Métodos
const pessoa = {
    nome: ' Maria',
    saudar() { console.log(`Ola, $(this.nome)`)}
}
```

<br>

### Spread Operator
```js
// Arrays - copiar e adicionar
const original = [1, 2, 3];
const copia = [...original];
const expandido = [...original, 4, 5];

// Objetos - copiar e atualizar
const usuario = { nome: 'Joao', idade: 30 };
const atualizado = { ...usuario, idade: 31 };

// Combinar arrays
const arr1 = [1, 2];
const arr2 = [3, 4];
const junto = [...arr1, arr2]; // [1, 2, 3, 4]
```

### Destructuring
Desestruturação
```js
// Arrays
const [primeiro, segundo] = [1, 2, 3];
console.log(primeiro); // 1

// Objetos
const usuario = { nome: 'Joao', idade: 30 };
const { nome, idade} = usuario;
console.log(nome); // 'Joao'

// Parâmetros de função (React props!)
function Componente({ titulo, descricao }) {
    console.log(titulo);
}

Componente({ Titulo: 'Olá', descricao: 'Mudno' });
```

<br>

## Modulo V - APIs: Fetch [GET/POST/PUT/DELETE]

### Consumindo API com Fetch
**Promises**: "uma promessa de acesso" que contém 3 estados: pendente (enquanto está executnado), resolvida(com dados ou sem dados), rejeitado (interrompida no meio do processo.)
```js
// GET - Buscar dados
// Função assincrona retorna uma promise
async function buscarUsuarios() {
    try {
        const response = await fetch('https://api.exemplo.com/usuarios');

        if (!response.ok) {
            throw new Error('Erro na requisição');
        }

        const dados = await response.json();
        console.log(dados);
    } catch (erro) {
        console.log('Erro: ', erro);
    }
}

buscarUsuarios();
```

### POST e PUT
```js
async function criarUsuario(usuario) {
    const response = await fetch('http...', {
        method: 'POST',
        headers: { 'Contente-Type': 'application/json' }

    })
}
```