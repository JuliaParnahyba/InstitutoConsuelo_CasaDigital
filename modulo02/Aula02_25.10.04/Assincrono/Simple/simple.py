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

def reading_txt(in_path, out_path):
    count_words=0
    big_words=0

    with open(in_path, 'r') as file:
        for line in file:
            word = line.strip()

            if not word:
                continue

            count_words += 1

            if len(word) > 5:
                big_words += 1

    if count_words > 0:
        percents = (big_words * 100) / count_words
    else:
        percents = 0

    data_py = {
        "total_palavras": count_words,
        "palavras_grandes": big_words,
        "porcentagem": round(percents, 2)
    }

    json_string = json.dumps(data_py, indent=4, ensure_ascii=False)

    with open(out_path, 'w') as json_file:
        json.dump(data_py, json_file, ensure_ascii=False, indent=4)

    print(json_string)
    return data_py

reading_txt(file_path, json_path)

