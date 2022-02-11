
class Conta:#classe
    def __init__(self, numero, titular, saldo, limite):#função construtora
        print("Construindo objeto...{}".format(self))
        self.__numero = numero#objeto # o "__" deixa o atributo privado
        self.__titular = titular#objeto
        self.__saldo = saldo#objeto
        self.__limite = limite#objeto


    def extrato(self):#metodo
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_saque

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.saca(valor)

    @property #Criação de um getter. getter sempre tem que ter um retorno
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter #Criação de um setter.
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_banco():
        return {'BB':'001', 'Caixa':'104', 'bradesco':'237'}
