

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite


    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular`{self.__titular}")


    def deposita(self, valor):
        self.__saldo += valor




    def __pode_sacar(self, valor_a_sacar):
        valor_diponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_diponivel
          




    def saca(self, valor):
        if (self.pode_sacar):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


    @property
    def saldo(self):
        return self.__saldo


    @property
    def titular(self):
        return self.__titular


    @property
    def limite(self):
        return self.__limite


    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    
    

        