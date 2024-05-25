class Base:
    def __init__(self, marca, modelo, anofabrica, preco, exibirinfo):
        self.marca = marca
        self.modelo = modelo
        self.anofabrica = anofabrica
        self.preco = preco


    def exibirinfo(self):
        print(f'o veiculo da {self.marca}, ano {self.anofabrica}, modelo {self.modelo}, custa {self.preco}')



class Carro(Base):
    def __init__(self, marca, modelo, anofabrica, preco, exibirinfo, numposta, conpustivel):
        super().__init__(marca, modelo, anofabrica, preco, exibirinfo)
        self.numposta = numposta
        self.conpustivel = conpustivel

class Moto(Base):
    def __init__(self, marca, modelo, anofabrica, preco, exibirinfo, cilindrada, tipopartida):
        super().__init__(marca, modelo, anofabrica, preco, exibirinfo)
        self.cilidranda = cilindrada
        self.tipopartida = tipopartida

class Concessionaria:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.__listadeveiculos = []
    
    def addveiculos(self, Base):
        self.__listadeveiculos.append(Base)
        print('veiculo adicionado com sucesso')

    def listatodosveiculos(self):
        for Base in self.__listadeveiculos:
            Base.exibirinfo()


pedraoveiculos = Concessionaria('PEDRÃO VEICULOS', 'RUA XEIRO DO QUEIJO, 121')

moto1 = Moto('HONDA', 'PCX', '2013', '16.400', 'a nova PCX apresenta um design imponente', '156,9 cc', 'Elétrico')
moto1.exibirinfo()



