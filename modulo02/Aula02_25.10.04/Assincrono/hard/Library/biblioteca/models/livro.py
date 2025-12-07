class Livro:
    def __init__(self, id_livro, titulo, autor, ano):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

        self.disponivel = True
        self.emprestado_para = None
        self.data_emprestimo = None
        self.data_devolucao = None
        self.historico_emprestimos = [] # lista de dicts com dados de empréstimos anteriores
        self.quantidade_emprestimos = 0
    
    @classmethod
    def from_dict(cls, dados):
        """
        Método para popular o objeto Livro a partir de um dicionário.
        """
        livro = cls(
            id_livro=dados["id_livro"],
            titulo=dados["titulo"],
            autor=dados["autor"],
            ano=dados["ano"]
        )

        # Campos de estado:
        livro.disponivel = dados.get("disponivel", True)
        livro.emprestado_para = dados.get("emprestado_para", None)
        livro.data_emprestimo = dados.get("data_emprestimo", None)
        livro.data_devolucao = dados.get("data_devolucao", None)
        livro.quantidade_emprestimos = dados.get("quantidade_emprestimos", 0)
        livro.historico_emprestimos = dados.get("historico_emprestimos", [])

        return livro
    

    def to_dict(self):
        """
        Método para converter o objeto Livro em um dicionário para ser salvo em JSON.
        """
        return {
            "id_livro": self.id_livro,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "disponivel": self.disponivel,
            "emprestado_para": self.emprestado_para,            # ID do usuário
            "data_emprestimo": self.data_emprestimo,
            "data_devolucao": self.data_devolucao,
            "quantidade_emprestimos": self.quantidade_emprestimos,
            "historico_emprestimos": self.historico_emprestimos, # lista de dicts
        }