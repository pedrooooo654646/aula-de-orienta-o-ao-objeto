# #características : soma, multiplicar, dividir, subtrair
# #ações : soma, multiplicação, divisão, subtração

class Calcuradora:
    def __init__(self):
       print('calcuradora feita')

    def somar(self, num1, num2):
        return num1 + num2

    def vezes(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        return num1 / num2
    
    def subtrair(self, num1, num2):
        if (num2 == 0):
         return 'divisão por 0 não é possivel'
        else:
           return num1 - num2
     


calcuradoradopedro = Calcuradora()
print(calcuradoradopedro.dividir(2,2))