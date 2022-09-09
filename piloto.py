from pessoa import Pessoa


from pessoa import Pessoa


class Piloto(Pessoa):
    '''
    Classe para representar piloto de vôo aéreo
    '''
    def __init__(self, matricula, horas_de_voo, habilitacao, exame_medico, nome, rg, cpf, idade, sexo):
        self.matricula = matricula
        self.horas_de_voo = horas_de_voo
        self.habilitacao = habilitacao
        self.exame_medico = exame_medico
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.idade = idade
        self.sexo = sexo
