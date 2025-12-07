import json

class Persistencia:
    """
    Classe responsável apenas por carregar e salvar dados em JSON.
    A Biblioteca usa esta classe, mas não sabe como o JSON é estruturado.
    """

    @staticmethod
    def carregar_livros(path):
        try:
            with open(path, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print(f"AVISO: Arquivo de livros não encontrado em: {path}")
            return []

    @staticmethod
    def carregar_usuarios(path):
        try:
            with open(path, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print(f"AVISO: Arquivo de usuários não encontrado em: {path}")
            return []
    
    @staticmethod
    def salvar_livros(path, lista_livros):
        with open(path, "w", encoding="utf-8") as arquivo:
            json.dump(lista_livros, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def salvar_usuarios(path, lista_usuarios):
        with open(path, "w", encoding="utf-8") as arquivo:
            json.dump(lista_usuarios, arquivo, indent=4, ensure_ascii=False)