

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf
    
    def cumprimentar (self):
        print(f'olá ! tudo bem? me chamo {self.nome}')

    
    def setcpf(self, novocpf):
        self.__cpf = novocpf

    def getcpf(self):
        return self.__cpf
    
class Mae(Pessoa):
    def __init__(self, nome, cpf, corpele):
        super().__init__(nome, cpf)
        self.corpele = corpele
    
    def dançar(self):
        print(f'{self.nome} está dançando')


# instÂncia de um objeto da classe pessoa

pessoa1 =Pessoa('tim maia', '000.111.222-33')

print(pessoa1.nome)
print(pessoa1.getcpf())

pessoa1.nome = 'glauber'

print(pessoa1.nome)
pessoa1.setcpf('111.222.333-44')
print(pessoa1.getcpf())