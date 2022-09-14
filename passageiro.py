from pessoa import Pessoa


class Passageiro(Pessoa):
    '''
    Classe para representar um passageiro
    '''
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade