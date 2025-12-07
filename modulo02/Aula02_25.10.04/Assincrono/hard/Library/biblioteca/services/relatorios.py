import csv

class RelatorioBiblioteca:
    @staticmethod
    def livros_mais_emprestados(self, caminho_csv, limite=None):
        """
        Gera um relatório CSV com os livros mais emprestados.

        - Ordena os livros por quantidade_emprestimos (decrescente).
        - Opcionalmente limita a quantidade de linhas.
        - Ignora livros que nunca foram emprestados (quantidade_emprestimos == 0).
        """
        # Filtrar livros que já foram emprestados
        livros_com_emprestimos = []
        for livro in self.livros:
            if livro.quantidade_emprestimos > 0:
                livros_com_emprestimos.append(livro)

        if not livros_com_emprestimos:
            print("Não há livros com empréstimos para gerar relatório.")
            return False

        # Ordenar por quantidade_emprestimos (do maior para o menor)
        livros_ordenados = sorted(
            livros_com_emprestimos,
            key=lambda l: l.quantidade_emprestimos,
            reverse=True,
        )

        # Aplicar limite (se informado)
        if limite is not None:
            livros_ordenados = livros_ordenados[:limite]

        # Escrever arquivo CSV
        try:
            with open(caminho_csv, "w", newline="", encoding="utf-8") as arquivo_csv:
                escritor = csv.writer(arquivo_csv)

                # Cabeçalho
                escritor.writerow(
                    ["id_livro", "titulo", "autor", "ano", "quantidade_emprestimos"]
                )

                # Linhas de dados
                for livro in livros_ordenados:
                    escritor.writerow(
                        [
                            livro.id_livro,
                            livro.titulo,
                            livro.autor,
                            livro.ano,
                            livro.quantidade_emprestimos,
                        ]
                    )

            print(f"Relatório gerado em: {caminho_csv}")
            return True

        except Exception as e:
            print(f"Erro ao gerar relatório CSV: {e}")
            return False