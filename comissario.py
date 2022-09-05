class Comissario():
    '''
    Classe para representar um comissário ou comissária de bordo
    '''
    def __init__(self, matricula, nome, funcao, horas_voo):
        self.matricula =matricula
        self.nome =nome
        self.funcao =funcao
        self.horas_voo =horas_voo
    def adiciona_hora(self,horas):
        self.horas_voo += horas
        pass