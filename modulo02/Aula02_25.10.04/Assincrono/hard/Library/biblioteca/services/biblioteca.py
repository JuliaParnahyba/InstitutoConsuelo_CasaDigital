import json
import csv

from biblioteca.models.livro import Livro
from biblioteca.models.usuario import Usuario
from biblioteca.storage.persistencia import Persistencia as PersistenciaJSON


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    # ----- Persistência de Dados (JSON) -----
    def carregar_dados(self, path_livros, path_usuarios):
        self.livros = []
        self.usuarios = []

        # Carregar dados crus
        dados_livros = PersistenciaJSON.carregar_livros(path_livros)
        dados_usuarios = PersistenciaJSON.carregar_usuarios(path_usuarios)

        # Converter dicionários em objetos
        for dados in dados_livros:
            self.livros.append(Livro.from_dict(dados))

        for dados in dados_usuarios:
            self.usuarios.append(Usuario.from_dict(dados))

        print(f"Dados carregados com sucesso de:\n- '{path_livros}'\n- '{path_usuarios}'.")

    # ----- Operações da Biblioteca -----
    # Cadastrar livro e usuário
    def cadastrar_livro(self, id_livro, titulo, autor, ano):
        """
        Método para cadastrar um novo livro na biblioteca.
        Cria um novo objeto Livro e o adiciona à coleção de livros.
        """
        novo_livro = Livro(id_livro, titulo, autor, ano)
        for livro in self.livros:
            if livro.titulo == titulo and livro.autor == autor:
                print("Livro já cadastrado.")
                return None
        self.livros.append(novo_livro)
        return novo_livro

    def cadastrar_usuario(self, id_usuario, nome, email):
        """
        Método para cadastrar um novo usuário na biblioteca.
        Cria um novo objeto Usuario e o adiciona à coleção de usuários.
        """
        novo_usuario = Usuario(id_usuario, nome, email)
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.email == email:
                print(f"Usuário {usuario.nome} | {usuario.email}, já cadastrado.")
                return None
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def importar_livros_de_csv(self, caminho_csv, pular_cabecalho=True):
        """
        Importa livros a partir de um arquivo CSV.

        Espera-se que cada linha do CSV tenha o formato:
        id_livro,titulo,autor,ano

        - caminho_csv: caminho do arquivo CSV.
        - pular_cabecalho: se True, ignora a primeira linha (cabeçalho).
        """
        quantidade_total = 0
        quantidade_importados = 0
        quantidade_duplicados = 0
        quantidade_invalidos = 0

        try:
            with open(caminho_csv, "r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)

                # Pular a primeira linha (cabeçalho)
                if pular_cabecalho:
                    try:
                        next(leitor)
                    except StopIteration:
                        print("Arquivo CSV vazio.")
                        return False

                # Ler linha por linha
                for linha in leitor:
                    quantidade_total += 1

                    # Validação básica de quantidade de colunas
                    if len(linha) < 4:
                        print(f"Linha inválida (colunas insuficientes): {linha}")
                        quantidade_invalidos += 1
                        continue

                    # Extrair campos
                    id_str = linha[0]
                    titulo = linha[1]
                    autor = linha[2]
                    ano_str = linha[3]

                    # Converter tipos (tentamos garantir que id e ano sejam inteiros)
                    try:
                        id_livro = int(id_str)
                        ano = int(ano_str)
                    except ValueError:
                        print(f"Linha inválida (ID ou ano não numérico): {linha}")
                        quantidade_invalidos += 1
                        continue

                    # Usar a própria lógica de cadastro para evitar duplicados
                    livro_existente = self.buscar_livro(id_livro=id_livro)
                    if livro_existente is not None:
                        # Já existe livro com esse ID → considera duplicado
                        quantidade_duplicados += 1
                        continue

                    novo_livro = self.cadastrar_livro(
                        id_livro=id_livro,
                        titulo=titulo,
                        autor=autor,
                        ano=ano,
                    )

                    if novo_livro is not None:
                        quantidade_importados += 1
                    else:
                        # cadastrar_livro retornou None → livro duplicado por título/autor
                        quantidade_duplicados += 1

            print("\n=== Resultado da importação de livros ===")
            print(f"Arquivo: {caminho_csv}")
            print(f"Linhas lidas: {quantidade_total}")
            print(f"Importados: {quantidade_importados}")
            print(f"Duplicados: {quantidade_duplicados}")
            print(f"Inválidos: {quantidade_invalidos}")

            return quantidade_importados > 0

        except FileNotFoundError:
            print(f"Erro: Arquivo CSV não encontrado em: {caminho_csv}")
            return False
        except Exception as erro:
            print(f"Erro inesperado ao importar CSV: {erro}")
            return False

    
    # Buscar livro e usuário
    def buscar_livro(self, titulo=None, id_livro=None):
        if not titulo and not id_livro:
            print("Por favor, forneça um dos parâmetros: título ou ID do livro.")
            return None

        if id_livro and titulo is None:
            for livro in self.livros:
                if livro.id_livro == id_livro:
                    return livro
            return None
        if titulo and id_livro is None:
            for livro in self.livros:
                if livro.titulo == titulo:
                    return livro
            return None
        elif titulo and id_livro:
            for livro in self.livros:
                if livro.titulo == titulo and livro.id_livro == id_livro:
                    return livro
            return None
    
    def buscar_usuario(self, nome=None, id_usuario=None):
        if not nome and not id_usuario:
            print("Por favor, forneça um dos parâmetros: nome ou ID do usuário.")
            return None
        
        if id_usuario and nome is None:
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    return usuario
            return None
        if nome and id_usuario is None:
            for usuario in self.usuarios:
                if usuario.nome == nome:
                    return usuario
            return None
        elif nome and id_usuario:
            for usuario in self.usuarios:
                if usuario.nome == nome and usuario.id_usuario == id_usuario:
                    return usuario
            return None
    
    # Empréstimo e devolução de livros
    def emprestar_livro(self, id_livro, id_usuario):
        """
        realizar empréstimo de livro para um usuário.
        """
        # Buscar livro e usuário
        livro = self.buscar_livro(id_livro=id_livro)
        usuario = self.buscar_usuario(id_usuario=id_usuario)

        if livro is None:
            print("Livro não encontrado.")
            return False

        if usuario is None:
            print("Usuário não encontrado.")
            return False

        if not livro.disponivel:
            print(f"O livro '{livro.titulo}' não está disponível para empréstimo.")
            return False

        # Realizar o empréstimo, atualizando o estado do livro
        livro.disponivel = False
        livro.emprestado_para = usuario.id_usuario
        livro.data_emprestimo = "2024-10-25"  # Data fixa para exemplo
        livro.data_devolucao = "2024-11-25"  # Data fixa para exemplo

        # Incrementar a contagem de empréstimos do livro
        livro.quantidade_emprestimos += 1

        # Adicionar livro à lista de empréstimos do usuário
        usuario.livros_emprestados.append(livro.id_livro)

        print(f"Empréstimo realizado:\n'{livro.titulo}', de {livro.autor} emprestado para {usuario.nome}.")
        return True
        
    def devolver_livro(self, id_livro, id_usuario):
        """
        Realizar a devolução de um livro por um usuário.
        """
        # Buscar livro e usuário
        livro = self.buscar_livro(id_livro=id_livro)
        usuario = self.buscar_usuario(id_usuario=id_usuario)

        if livro is None:
            print("Livro não encontrado para devolução.")
            return False

        if usuario is None:
            print("Usuário não encontrado para devolução.")
            return False

        # Verificar se o livro está disponível na biblioteca
        if livro.disponivel:
            print(f"O livro '{livro.titulo}' já está disponível na biblioteca.")
            return False

        # Verificar se o livro está emprestado para o usuário correto
        if livro.emprestado_para != usuario.id_usuario:
            print(f"O livro '{livro.titulo}' não foi emprestado para o usuário {usuario.nome}.")
            return False

        livro_encontrado = False
        for id_livro_emprestado in usuario.livros_emprestados:
            if id_livro_emprestado == id_livro:
                livro_encontrado = True
                break

        if not livro_encontrado:
            print(
                f"O livro '{livro.titulo}' não está registrado como emprestado para o usuário {usuario.nome}."
            )
            return False

        # Realizar a devolução, atualizando o estado do livro para disponível
        livro.disponivel = True
        livro.emprestado_para = None
        livro.data_emprestimo = None
        livro.data_devolucao = "2024-11-25"  # Data fixa para exemplo

        # Registrar histórico para o USUÁRIO
        registro_usuario = {
            "id_livro": livro.id_livro,
            "titulo": livro.titulo,
            "data_emprestimo": livro.data_emprestimo,
            "data_devolucao": livro.data_devolucao,
        }
        usuario.historico_emprestimos.append(registro_usuario)

        # Registrar histórico para o LIVRO
        registro_livro = {
            "id_usuario": usuario.id_usuario,
            "nome_usuario": usuario.nome,
            "data_emprestimo": livro.data_emprestimo,
            "data_devolucao": livro.data_devolucao,
        }
        livro.historico_emprestimos.append(registro_livro)

        # Remover o livro da lista de empréstimos do usuário
        nova_lista = []
        for id_livro_emprestado in usuario.livros_emprestados:
            if id_livro_emprestado != id_livro:
                nova_lista.append(id_livro_emprestado)
        usuario.livros_emprestados = nova_lista

        print(
            f"Devolução realizada:\n'{livro.titulo}', de {livro.autor} devolvido por {usuario.nome}."
        )
        return True


    def salvar_dados(self, path_livros, path_usuarios):
        lista_livros = [livro.to_dict() for livro in self.livros]
        lista_usuarios = [usuario.to_dict() for usuario in self.usuarios]

        PersistenciaJSON.salvar_livros(path_livros, lista_livros)
        PersistenciaJSON.salvar_usuarios(path_usuarios, lista_usuarios)

        print(f"Dados salvos em:\n- {path_livros}\n- {path_usuarios}")

