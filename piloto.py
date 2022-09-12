from pessoa import Pessoa


class Piloto(Pessoa):
    '''
    Classe para representar piloto de vôo aéreo
    '''
    def __init__(self, matricula, habilitacao, nome, cpf, idade):
        self.matricula = matricula
        self.habilitacao = habilitacao
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
