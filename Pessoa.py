# Autor: Henrique Rosa Carvalho
# Aula 09 - Encapsulamento

# Implementar as classes do diagrama, considerando os modificadores de acesso de cada atributo e método


class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print(self.nome)

    def __imprimeTelefone(self):
        print(self.__telefone)