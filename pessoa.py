
class Pessoa():
    '''
    Classe para representar uma pessoa
    '''
    def __init__(self, nome, cpf, sexo, pcd, telefone, dataNascimento, email, endereco):
        
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.sexo = sexo
        self.pcd = pcd
        self.dataNascimento = dataNascimento
        self.email = email
        self.endereco = endereco
        
    def exibe_informacoes(self):
      print(f'{self.nome} {self.email} {self.telefone} {self.endereco} {self.dataNascimento}')
        
pessoa1 = Pessoa(nome='ze', cpf=78945612345, sexo='M', pcd=False, telefone='8859862355', dataNascimento='31/12/1991', email='ze@mail.com', endereco='logo ali')

pessoa1.exibe_informacoes()
    
        