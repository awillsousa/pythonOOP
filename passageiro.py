from pessoa import Pessoa


class Passageiro(Pessoa):
    '''
    Classe para representar um passageiro
    '''
    def __init__(self, nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte):
        self.bagagem = bagagem
        self.identificador_voo = identificador_voo
        self.passaporte = passaporte
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.idade = idade
        self.sexo = sexo