class Base:
    def __init__(self, marca, modelo, anofabrica, preco):
        self.marca = marca
        self.modelo = modelo
        self.anofabrica = anofabrica
        self.preco = preco


    def exibirinfo(self):
        print(f'o veiculo da {self.marca}, ano {self.anofabrica}, modelo {self.modelo}, custa {self.preco}')

class Carro(Base):
    def __init__(self, marca, modelo, anofabrica, preco, numposta, conpustivel):
        super().__init__(marca, modelo, anofabrica, preco)
        self.numposta = numposta
        self.conpustivel = conpustivel
    def exibirinfo(self):
        print(f'o carro da {self.marca}, ano {self.anofabrica}, modelo {self.modelo}, custa {self.preco} esse carro possui {self.numposta} portas é movido a {self.conpustivel}')
        

class Moto(Base):
    def __init__(self, marca, modelo, anofabrica, preco, cilindrada, tipopartida):
        super().__init__(marca, modelo, anofabrica, preco)
        self.cilidranda = cilindrada
        self.tipopartida = tipopartida
    def exibirinfo(self):
        print(f'a moto da {self.marca}, ano {self.anofabrica}, modelo {self.modelo}, custa {self.preco} essa moto tem {self.cilidranda}, e a partida é {self.tipopartida}')

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

#minha conssionaria
pedraoveiculos = Concessionaria('PEDRÃO VEICULOS', 'RUA XEIRO DO QUEIJO, 121')

#motos
moto1 = Moto('HONDA', 'PCX-125', 2024, 16.400, '125 cc', 'Elétrico')
pedraoveiculos.addveiculos(moto1)
moto1.exibirinfo()

#carros
#marca, modelo, anofabrica, preco, exibirinfo, numposta, conpustivel
carro1 = Carro('Toyota', 'Corolla', 2020, 85000.0, 4, 'Gasolina')
pedraoveiculos.addveiculos(carro1)

carro2 = Carro('Ford', 'Mustang', 2019, 300000.0, 2, 'Gasolina')
pedraoveiculos.addveiculos(carro2)

carro3 = Carro('Chevrolet', 'Onix', 2021, 70000.0, 4, 'Flex')
pedraoveiculos.addveiculos(carro3)

carro4 = Carro('Hyundai', 'HB20', 2022, 75000.0, 4, 'Flex')
pedraoveiculos.addveiculos(carro4)

carro5 = Carro('Volkswagen', 'Golf', 2018, 90200.0, 4, 'Gasolina')
pedraoveiculos.addveiculos(carro5)




pedraoveiculos.listatodosveiculos()




