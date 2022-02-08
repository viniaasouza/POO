
class Conta:#classe
    def __init__(self, numero, titular, saldo, limite):#função construtora
        print("Construindo objeto...{}".format(self))
        self.numero = numero#objeto
        self.titular = titular#objeto
        self.saldo = saldo#objeto
        self.limite = limite#objeto

    def extrato(self):#metodo
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
