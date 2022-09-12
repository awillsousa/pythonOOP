from pessoa import Pessoa

class Comissario(Pessoa):
    '''
    Classe para representar um comissário ou comissária de bordo
    '''
    def __init__(self, nome, cpf, idade, pcd=False):        
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.pcd = pcd
        