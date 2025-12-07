"""
Desenvolva um sistema de notas que:

- Leia dados de alunos de um CSV (nome, nota1, nota2, nota3)
- Calcule a média de cada aluno
- Determine se foi aprovado (média ≥ 7.0)
- Gere um relatório em JSON com estatísticas da turma:
  - Quantidade de aprovados/reprovados
  - Média geral da turma
  - Maior e menor nota
- Use funções separadas para cada operação
"""
import os
import csv
import json

# Pede ao usuário o caminho do arquivo CSV
file_path = input("Informe o caminho do arquivo CSV (ex: ./notas_alunos.csv):\n").strip()

# Se o usuário apenas apertar Enter, usa um padrão
if not file_path:
  file_path = './notas_alunos.csv'

# Gera automaticamente o nome do JSON com base no nome do CSV
base_name, _ = os.path.splitext(file_path)
json_path = base_name + '_relatorio.json'

class Aluno:
  def __init__ (self, nome, notas):
    self.nome = nome
    self.notas = notas
    self.media = 0.0
    self.status = ''

  def calculo_media(self):
    self.media = sum(self.notas) / len(self.notas)
  
  def determinar_status(self):
    if self.media >= 7.0:
      self.status = 'Aprovado'
    else:
      self.status = 'Reprovado'
  
  def print_info(self):
    print(
      f'Aluno: {self.nome},'
      f'Notas: {self.notas},'
      f'Média: {self.media:.2f},'
      f'Status: {self.status}'
    )

# Função para gerar o relatório em JSON
def gerar_relatorio(alunos, out_path):
  total_alunos = len(alunos)

  if total_alunos == 0:
    print("Nenhum aluno para gerar relatório.")
    return
  
  if total_alunos == 1:
    print("A turma possui apenas um aluno. Estatísticas como média geral, maior e menor nota não podem ser calculadas.")
    return

  aprovados = 0
  reprovados = 0
  soma_medias = 0.0
  maior_nota = 0.0
  menor_nota = 0.0

  for aluno in alunos:
    if aluno.status == 'Aprovado':
      aprovados += 1
    if aluno.status == 'Reprovado':
      reprovados += 1
    soma_medias += aluno.media

  media_geral = soma_medias / total_alunos
  
  for aluno in alunos:
    if aluno.media > maior_nota:
      maior_nota = aluno.media
    if menor_nota == 0.0 or aluno.media < menor_nota:
      menor_nota = aluno.media

  relatorio = {
    'total_alunos': total_alunos,
    'aprovados': aprovados,
    'reprovados': reprovados,
    'media_geral': round(media_geral, 2),
    'maior_nota': round(maior_nota, 2),
    'menor_nota': round(menor_nota, 2),
    'alunos': [
      {
        'nome': aluno.nome,
        'notas': aluno.notas,
        'media': round(aluno.media, 2),
        'status': aluno.status
      } for aluno in alunos
    ]
  }

  print(f"\nRelatório da Turma:{relatorio}\n")

  with open(out_path, 'w', encoding='utf-8') as json_file:
    json.dump(relatorio, json_file, indent=4, ensure_ascii=False)


# Função para ler o arquivo CSV e processar os dados,
# capturando os dados necessários para o relatório
def leitor_csv(in_path):
  alunos = []                                   # Lista para armazenar os objetos Aluno

  with open(in_path, 'r', encoding='utf-8') as arquivo:           # Abra o arquivo CSV atribuindo à variável file 
    csv_arquivo = csv.reader(arquivo)           # Lê o arquivo CSV
    next(csv_arquivo)                           # Pula a primeira linha, isto é, o cabeçalho

    for linha in csv_arquivo:
      Aluno_nome = linha[0]                     # Captura o nome do aluno
      #print(Aluno_nome)

      Aluno_notas = linha[1:4]                  # Captura as notas de cada aluno
      for i in range(len(Aluno_notas)):         # Itera sobre cada nota
        Aluno_notas[i] = float(Aluno_notas[i])  # Converte cada nota para float
        #print(Aluno_notas)

      aluno = Aluno(Aluno_nome, Aluno_notas)    # Cria o objeto aluno
      aluno.calculo_media()                     # Calcula a média do aluno
      aluno.determinar_status()                 # Determina o status do aluno
      aluno.print_info()                        # Imprime as informações do aluno

      alunos.append(aluno)                      # Adiciona o objeto aluno à lista
  
  # Gera o relatório em JSON
  gerar_relatorio(alunos, json_path)

leitor_csv(file_path)