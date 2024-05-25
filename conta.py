# #características : saldo, titular, 
# #ações : depositar, sacar, verificar o saldo

class Conta:

    
    def __init__(self,titular: str, saldo: float=500):
        self.titular = titular
        self.__saldo = saldo
    def depositar(self, valordepositado: float):
        #depositarmoney = int(input('quanto dejesa depositar:'))
        self.__saldo = valordepositado + self.__saldo

    def sacar(self, valorsacado):
        #sacarmoney = int(input('quanto dejesa sacar:'))
        self.__saldo-valorsacado

    def verificarsaldo(self):
        return(f'{self.titular}senhor esse é seu saldo = R${self.__saldo}')


contapedro = Conta('pedro')


print(contapedro.verificarsaldo())

print(contapedro.saldo)
















































#conta01 = conta('0', 'pedro')

# print('----MENU----\n'
#       '1 - DEPOSITAR\n'
#       '2 - SACAR\n'
#       '3 - VERIFICAR\n')
# digite = int(input('DIGITE SUA OPÇÃO:'))
# if digite == 1:
#    conta01.depositar()
   