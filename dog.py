#características : temperamento, tamanho, raça, cor, nome
#ações : latir, pular, correr, comer

class dog:
    def __init__(self, temperamento, tamanho, raca, cor, nome):
        self.nome = nome
        self.temperamento = temperamento
        self.tamanho = tamanho
        self.raca = raca
        self.cor = cor

    def latir(self):
        print(f'{self.nome} está latindo')

dog01 = dog('malzinho', 'grande', 'SRD', 'ruivo e cinza e branco', 'K9')

dog01.latir()

print(dog01.temperamento)



