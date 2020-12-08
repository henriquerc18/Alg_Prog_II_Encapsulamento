from Pessoa import Pessoa

class Fisica (Pessoa):
    def __init__(self, nome, endereco, cpf, idade, peso, altura):
        Pessoa.__init__ (self, nome, endereco)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimeCPF(self):
        print(self.__cpf) 

    def __calculaIMC(self):
        valor_imc = self.peso/(self.altura ** 2) 
        return valor_imc      