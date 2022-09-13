from pessoa import Pessoa


class Comissario(Pessoa):
    '''
    Classe para representar um comissário ou comissária de bordo
    '''
    def __init__(self, matricula, idioma, nome, cpf, idade):
        self.matricula = matricula
        self.idioma = idioma
        self.nome = nome
        self.cpf = cpf
        self.idade = idade