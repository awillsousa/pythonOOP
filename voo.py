from comissario import comissario
class Voo():
    '''
    Classe para representar um vôo aéreo
    '''
    def __init__(self, aviao, aeropt_partida, dt_partida, hr_partida, aeropt_chegada, dt_chegada, hr_chegada,comissario, piloto, passageiros ):
        self.aviao=[aviao] #Identificação, capacidade
        self.aeropt_partida=aeropt_partida
        self.dt_partida=dt_partida
        self.hr_partida=hr_partida
        self.aeropt_chegada=aeropt_chegada
        self.dt_chegada=dt_chegada
        self.hr_chegada=hr_chegada
        self.tripulacao = {comissario:[comissario],piloto:[piloto]} #comissario
        self.passageiros = passageiros

        pass

    