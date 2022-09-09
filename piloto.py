from pessoa import Pessoa

class Piloto(Pessoa):
    '''
    Classe para representar piloto de vôo aéreo
    '''
    def __init__(self, nome, cpf, idade, num_breve):
        self.pcd = False
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.num_breve = num_breve
    

        
