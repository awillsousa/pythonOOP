
from assento import *

class Voo():
    '''
    Classe para representar um vôo aéreo
    '''
    def __init__(self, numero, origem, destino, horario_partida,
                 duracao_estimada, tarifa_basica, piloto, copiloto,
                 comissarios_voo):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.horario_partida = horario_partida
        self.duracao_estimada = duracao_estimada
        self.tarifa_basica = tarifa_basica
       
       #interação com as outras classes
        self.piloto = piloto
        self.copiloto = copiloto
        self.comissarios_voo = comissarios_voo
        
        #assentos
        self.assentos = []
        self.define_mapa_assentos()
        
    def assento_valido(self, fila, poltrona):
        if fila >= len(self.assentos) or fila < 0:
            return False
        elif poltrona >= len(self.assentos[0]) or poltrona < 0:
            return False
        
        return True
    
    def assento_ocupado(self, fila, poltrona):
        return self.assentos[fila][poltrona].ocupado
    
    def ocupa_assento(self, fila, poltrona, passageiro):
        self.assentos[fila][poltrona].ocupa_assento(passageiro)
        
    def desocupa_assento(self, fila, poltrona):
        self.assentos[fila][poltrona].desocupa_assento()
        pass

    