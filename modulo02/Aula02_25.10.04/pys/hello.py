first = "Hello"
second = "World"
year = 2025
born = 1990

print(first + " " + second)
print(f"Now is the year {year}")

print(type(first))
print(type(year))

print("\nusando com range iniciando com 0")
for i in range(5):
    print(i)

print("\nusando com range iniciando com 1")
for i in range(5):
    print(i + 1)

print("\nusando com range iniciando de um determinado nº até o lenght determinado")
for i in range(2, 5):
    print(i)

frutas = ["maçã", "banana", "laranja"]
print("\nusando com range para percorrer uma lista")
for fruta in frutas:
    print(f"A fruta é: {fruta}")

print("\nusando com range para percorrer uma lista com índice")
for indice, fruta in enumerate(frutas):
    print(f"A fruta no índice {indice} é: {fruta}")

print("\niniciando uma lista vazia e preenchendo com nº pares ao quadrado.\nModelo tradicional")
#Tradicional
numeros_tradicional = []
for i in range(10):
    if i % 2 == 0:
        numeros_tradicional.append(i ** 2)
print(numeros_tradicional)

print("\niniciando uma lista vazia e preenchendo com nº pares ao quadrado.\nModelo com Comprehesion")
#Comprehesion
numeros_comprehesion = [i ** 2 for i in range(10) if i % 2 == 0]
print(numeros_comprehesion)
