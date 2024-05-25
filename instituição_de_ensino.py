# #características :   
# #ações : adicionar livros, listar livros


class Livro:
    def __init__(self, titulo, autor, ano, status):
        '''cria um objeto da classe livro com os atribuutos solicitadas'''
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status
    
    def setdisponivel(self):
        self.status = 'disponivel'
    
    def setindisponivel(self):
        self.status = 'indisponivel'   





class Biblioteca: 
    def __init__(self):
        '''agrupa objetos da classe livro'''
        self.lista=[]
        
    def addlivro(self, objetolivro):
        self.lista.append(objetolivro)
        return 'o livro foi adicionado'
    
    def listarlivros(self):
        for livro in self.lista:
            print(f'TÍTULO : {livro.titulo} | AUTOR : {livro.autor} | ANO : {livro.ano} | DISPONIBILIDADE : {livro.status}')

    def emprestarlivro(self, titulolivro):
        for livro in self.lista:
            if livro.titulo == titulolivro:
                livro.setindisponivel()
                print(f'O Livro {livro.titulo} foi emprestado com sucesso, o seu status agora é indisponivel\n')




livro1 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "disponivel\n")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "disponivel\n")

mybli = Biblioteca()

mybli.addlivro(livro1)
mybli.addlivro(livro2)

# print(mybli.lista)
mybli.listarlivros()
mybli.emprestarlivro('Cem Anos de Solidão')
# print(mybli.lista)
mybli.listarlivros()