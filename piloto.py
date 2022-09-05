class Piloto():
    '''
    Classe para representar piloto de vôo aéreo
    '''
    def __init__(self, matricula, nome, funcao, horas_voo):
        self.matricula =matricula
        self.nome =nome
        self.funcao =funcao
        self.horas_voo =horas_voo
        pass

    def adiciona_hora(self,horas):
        self.horas_voo += horas
        pass
