

class Trouxa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf
    
    def cumprimentar (self):
        print(f'olá ! tudo bem? me chamo {self.nome}')

    
    def setcpf(self, novocpf):
        self.__cpf = novocpf

    def getcpf(self):
        return self.__cpf
    


class Bruxo:
    def __init__(self, casa, patrono):
        self.casa = casa
        self.patrono = patrono

    def lancarfeitco(self):
        print('solta o fetiço')



class Mestico(Trouxa, Bruxo):
    def __init__(self, nome, cpf, casa, patrono):
        super().__init__(nome, cpf)
        Bruxo.__init__(self, casa, patrono)


mestico1 = Mestico('luna', '000.111.222-33', 'grifinoria', 'coelho')

mestico1.lancarfeitco()





