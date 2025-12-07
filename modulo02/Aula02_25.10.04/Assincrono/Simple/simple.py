"""
Crie um programa que:

- Leia um arquivo de texto com uma lista de palavras (uma por linha)
- Conte quantas palavras têm mais de 5 letras
- Salve o resultado em um arquivo JSON com o formato:

```json
{
    "total_palavras": 100,
    "palavras_grandes": 45,
    "porcentagem": 45.0
}
```
"""

import json

file_path = './text.txt'
json_path = './result.json'

# Funcao para ler o arquivo de texto e gerar o JSON
def reading_txt(in_path, out_path):
    count_words=0   # contador de palavras
    big_words=0     # contador de palavras com mais de 5 letras

    # Leitura do arquivo de texto
    with open(in_path, 'r') as file:    # abre o arquivo para leitura
        for line in file:               # itera sobre cada linha do arquivo
            word = line.strip()         # remove espaços em branco e quebras de linha

            if not word:                # se a linha estiver vazia,
                continue                # pula para a próxima iteração

            count_words += 1            # incrementa o contador de palavras

            if len(word) > 5:           # verifica se a palavra tem mais de 5 letras
                big_words += 1          # incrementa o contador de palavras grandes

    # Cálculo da porcentagem de palavras grandes    
    if count_words > 0:                             # se houver palavras lidas
        percents = (big_words * 100) / count_words  # calcula a porcentagem de palavras grandes
    else:                                           # se não houver palavras lidas
        percents = 0                                # define a porcentagem como 0

    # Criação do dicionário com os dados
    data_py = {
        "total_palavras": count_words,
        "palavras_grandes": big_words,
        "porcentagem": round(percents, 2)
    }

    # Escrita do dicionário em um arquivo JSON
    json_string = json.dumps(data_py, indent=4, ensure_ascii=False) # converte o dicionário para uma string JSON formatada

    # Salva o JSON em um arquivo
    with open(out_path, 'w') as json_file:                          # abre o arquivo JSON para escrita
        json.dump(data_py, json_file, ensure_ascii=False, indent=4) # escreve o dicionário no arquivo JSON

    # Exibe o JSON gerado
    print(json_string)

    # Retorna o dicionário com os dados
    return data_py

# Chama a função para ler o arquivo de texto e gerar o JSON
reading_txt(file_path, json_path)

