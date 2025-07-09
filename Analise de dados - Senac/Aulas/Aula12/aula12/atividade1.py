import pandas as pd

livros = ['Literatura Brasileira', 'Literatura Estrangeira', 'Ciências', 'Matemática', 'Historia']
quantidade_livros = [12, 9, 18, 14, 20]
biblioteca = pd.Series(quantidade_livros, index=livros)


emprestados_quant = [4, 2, 7, 5, 6]
emprestados = pd.Series(emprestados_quant, index=livros)
nova_biblioteca = (biblioteca - emprestados)
nova_biblioteca.loc['Filosofia'] = None

print("Livros na Biblioteca:")
print(nova_biblioteca)
print(" ")
print("Livros para serem emprestados:")
print(nova_biblioteca[nova_biblioteca > 1])
print(" ")
print("Categorias com mais de 5 livros:")
print(nova_biblioteca[nova_biblioteca > 5])
print("")
