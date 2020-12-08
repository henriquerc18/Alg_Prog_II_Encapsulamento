from Pessoa import Pessoa

class Juridica (Pessoa):
    def __init__(self, nome, endereco, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__ (self, nome, endereco)
        self.__cnpj = cnpj
        self.__inscricaoEstadual  = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print(self.__cnpj) 

    def __emitirNotaFiscal(self):
        print("Nota Fiscal nº: ")       