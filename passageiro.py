from pessoa import Pessoa

class Passageiro(Pessoa):
    '''
    Classe para representar um passageiro
    '''
    def __init__(self, nome, idade, cpf, pcd=False):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.pcd = pcd     
