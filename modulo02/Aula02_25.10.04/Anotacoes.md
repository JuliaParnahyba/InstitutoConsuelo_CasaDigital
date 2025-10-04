# Python na Cozinha: Preparando os Dados

Paython é uma linguagem de tipagem dinâmica, sendo o tipo de variável deverminado no momento da sua declaração. 

## List Comprehensions
Forma concisa de criar listas, sendo mais rápida que os loops tradicionais, mais legíve para operações simples e com menos código. 

```py
#Tradicional
numeros = []
for i in range(10):
    if i % 2 == 0
        numeros.append(i ** 2)

#Comprehesion
numeros = [i ** 2 for i in range(10) if i % 2 == 0]
print numeros
```

## Escopos
Local: dentro de uma função - dentro de def
Global: no níel do módulo - fora de def
Built-in: nome pré-definidos no Python