from mini_biblioteca.emprestimos import Emprestimo
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario


def main():
    usuario = Usuario("Maria", "u1")
    livro = Livro("Dom Casmurro", "Machado de Assis", "L001")

    emprestimo = Emprestimo(livro, usuario)
    print(f"Empréstimo feito: {usuario.nome} pegou '{livro.titulo}'")
    print(f"Livro disponível? {livro.disponivel} | empréstimo ativo? {emprestimo.ativo}")

    emprestimo.devolver()
    print(f"Após devolver -> disponível: {livro.disponivel} | ativo: {emprestimo.ativo}")


if __name__ == "__main__":
    main()
