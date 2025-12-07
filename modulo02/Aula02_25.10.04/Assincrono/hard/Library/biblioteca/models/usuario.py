class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
    
        self.livros_emprestados = []
        self.historico_emprestimos = [] # lista de dicts com dados históricos de empréstimos
    

    @classmethod
    def from_dict(cls, dados):
        """
        Método para popular o objeto Usuario a partir de um dicionário.
        """
        usuario = cls(
            id_usuario=dados["id_usuario"],
            nome=dados["nome"],
            email=dados["email"]
        )

        # Campos de estado:
        usuario.livros_emprestados = dados.get("livros_emprestados", [])
        usuario.historico_emprestimos = dados.get("historico_emprestimos", [])

        return usuario

    def to_dict(self):
        """
        Método para converter o objeto Usuario em um dicionário para ser salvo em JSON.
        """
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "email": self.email,
            "livros_emprestados": self.livros_emprestados,       # lista de IDs de livros
            "historico_emprestimos": self.historico_emprestimos, # lista de dicts
        }
