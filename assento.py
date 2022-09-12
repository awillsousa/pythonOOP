class Assento():
    '''
    Classe para representar um assento
    '''
    def __init__(self, assento_num, valor_passagem):
        self.poltronanum = assento_num
        self.ocupado = False
        self.passageiro = =none

    def ocupa_assento(self,passageiro):
        self.passgeiro = passageiro
    
    def desocupa_asssento(self):
        self.passgeiro = none

class AssentoBasico(Assento):
    '''
    Classe para representar um assento
    '''
    def __init__(self, assento_num):
        self.poltronanum = assento_num

class AssentoConfort(Assento):
    '''
    Classe para representar um assento mais caro
    '''
    def __init__(self, assento_num):
        self.poltronanum = assento_num
        

class AssentoEmergencia(Assento):
    '''
    Classe para representar um assento de emergencia
    '''
    def __init__(self, assento_num):
        self.poltronanum = assento_num

class AssentoReservado(Assento):
    '''
    Classe para representar um assento reservado para 
    passageiros como idosos ou pessoas com crianças
    de colo
    '''
    def __init__(self, assento_num):
        self.poltronanum = assento_num
