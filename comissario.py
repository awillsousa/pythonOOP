from pessoa import Pessoa

class Comissario(Pessoa):
    '''
    Classe para representar um comissário ou comissária de bordo
    '''
    def __init__(self, nome, idade, cpf, pcd=False):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.pcd = pcd