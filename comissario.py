from pessoa import Pessoa


class Comissario(Pessoa):
    '''
    Classe para representar um comissário ou comissária de bordo
    '''
    def __init__(self, tipo_de_voo, idioma, nome, rg, cpf, idade, sexo):
        self.tipo_de_voo = tipo_de_voo
        self.idioma = idioma
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.idade = idade
        self.sexo = sexo