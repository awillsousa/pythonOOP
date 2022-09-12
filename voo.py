from assento import *

class Voo():
    '''
    Classe para representar um vôo aéreo
    '''
    def __init__(self, horario, identificador_aeronave, tarifa_basica, origem, destino, duracao, comissarios_voo, assentos, piloto, copiloto, comissario):
        self.horario = horario
        self.identificador_aeronave = identificador_aeronave
        self.origem = origem
        self.destino = destino
        self.duracao = duracao
        self.tarifa_basica = tarifa_basica
        
        self.piloto = piloto
        self.copiloto = copiloto
        self.comissarios_voo = comissarios_voo

        self.assentos = self.define_mapa_assentos[]

    def ocupa_assento(self,fila, poltrona, passageiro):
        self.assentos[fila][poltrona].ocupa_assento(passageiro)

    def desocupa_assento(self,fila, poltrona):
        self.assentos[fila][poltrona].desocupa_assento()

    def define_mapa_assentos(self, num_filas=10, num_poltronas_por_fila=6):
    
    for fila in range(num_filas):
        assentos.append([])
        for poltrona in range(6):

            if fila == 0:
                assento_reservado = AssentoReservado(tarifa_basica)
                assentos[fila].append(assento_reservado)

            elif fila == 5:
                assento_emergencia = AssentoEmergencia(400)
                assentos[fila].append(assento_emergencia)

            elif fila in [7,8]:
                assento_confort = AssentoConfort(tarifa_basica, extra=100)
                assentos[fila].append(assento_confort)
    
            else:
                assento_basico = AssentoBasico(tarifa_basica)
                assentos[fila].append(assento_basico)
    
    def exibe_assentos(self):
    filas = len(self.assentos)
    poltronas = len(self.assentos[0])

    corredor = "||     |"
    line = '-'*(9*poltronas+3)

    print("RES - RESERVADO")
    print("BAS - BÁSICO")
    print("EME - EMERGÊNCIA")
    print("CON - CONFORT")
    
    print("MAPA DE ASSENTOS".center(len(line)))
    for f in range(filas):
        print(line)
        seq_poltronas = ""
        for p in range(poltronas):
            tipo_assento = self.assentos[f][p].tipo
            ocupado = self.assentos[f][p].ocupado

            if p == poltronas//2:
            seq_poltronas += corredor
            
            if ocupado:
                seq_poltronas += f"| XXXXX "
            elif tipo_assento == 'EMERGENCIA':
                seq_poltronas += f"| <{tipo_assento[0:3]}> "
            elif tipo_assento == 'RESERVADO':
                seq_poltronas += f"| -{tipo_assento[0:3]}- "
            elif tipo_assento == 'CONFORT':
                seq_poltronas += f"| ${tipo_assento[0:3]}$ "
            else:
                seq_poltronas += f"|  {tipo_assento[0:3]}  "

        seq_poltronas += "|"
        print(seq_poltronas)

    print(line);