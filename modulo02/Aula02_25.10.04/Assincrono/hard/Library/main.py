from biblioteca.services import Biblioteca
from biblioteca.services.relatorios import RelatorioBiblioteca  # se você já criou


def main():
    biblioteca = Biblioteca()

    # Carregar dados existentes (se quiser começar de algum estado)
    biblioteca.carregar_dados("data/livros.json", "data/usuarios.json")

    print("\n=== Importando livros a partir de CSV ===")
    biblioteca.importar_livros_de_csv("data/livros_importados.csv")

    print("\nTotal de livros após importação:", len(biblioteca.livros))

    # Opcional: salvar novamente o JSON com os livros novos
    biblioteca.salvar_dados("data/livros.json", "data/usuarios.json")

    # Opcional: gerar relatório atualizado
    RelatorioBiblioteca.livros_mais_emprestados(
        biblioteca,
        "data/relatorio_livros_mais_emprestados.csv",
        limite=10,
    )


if __name__ == "__main__":
    main()
