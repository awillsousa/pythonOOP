class Assento():
    '''
    Classe para representar um assento
    '''
    def __init__(self):
        pass

class AssentoBasico(Assento):
    '''
    Classe para representar um assento
    '''
    def __init__(self):
        pass

class AssentoConfort(Assento):
    '''
    Classe para representar um assento mais caro
    '''
    def __init__(self):
        pass

class AssentoEmergencia(Assento):
    '''
    Classe para representar um assento de emergencia
    '''
    def __init__(self):
        pass

class AssentoReservado(Assento):
    '''
    Classe para representar um assento reservado para 
    passageiros como idosos ou pessoas com crianças
    de colo
    '''
    def __init__(self, poltronanum):
        self.poltronanum = poltronanum
        pass
