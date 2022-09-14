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

       # interação com as outras classes
       self.piloto = piloto
       self.copiloto = copiloto
       self.comissarios_voo = comissarios_voo
       
       # define os assentos do vôo
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

    def define_mapa_assentos(self, num_filas=10, num_poltronas_por_fila=6):

        for fila in range(num_filas):  # 10 filas
            self.assentos.append([])
            for poltrona in range(num_poltronas_por_fila): # 6 poltronas por fila

                if fila == 0:  # assentos da fila 1 são todos reservados
                    assento_reservado = AssentoReservado(self.tarifa_basica)
                    self.assentos[fila].append(assento_reservado)

                elif fila == 5: # assentos da fila 6 são assentos de emergência
                    assento_emergencia = AssentoEmergencia(self.tarifa_basica)
                    self.assentos[fila].append(assento_emergencia)

                elif fila in [7,8]: # assentos das filas 8 e 9 são confort ($$$)
                    assento_confort = AssentoConfort(self.tarifa_basica, extra=100)
                    self.assentos[fila].append(assento_confort)
                
                else:  # os demais assentos são todos básicos
                    assento_basico = AssentoBasico(self.tarifa_basica)
                    self.assentos[fila].append(assento_basico)

    def exibe_assentos(self):
        filas = len(self.assentos)
        poltronas = len(self.assentos[0])

        corredor = "||     |"
        line = '-'*(9*poltronas+3)
        print("Tipos de Assentos: ")
        print("\tRES - RESERVADO")
        print("\tBAS - BÁSICO")
        print("\tEME - EMERGÊNCIA")
        print("\tCON - CONFORT\n")
        
        print("MAPA DE ASSENTOS".center(len(line)))
        # exibe os números das posições das poltronas
        linha_num_poltronas = "   "
        for p in range(poltronas):
            linha_num_poltronas += f"{p+1}".center(8)
            if p+1 == poltronas//2:
                linha_num_poltronas += "        "
                
        print(linha_num_poltronas)

        # exibe as poltronas nas filas
        for f in range(filas):
            print(line)
            seq_poltronas = f"{f+1} "
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

        print(line)

    def exibe_informacoes(self):
        print(f"Voo: {self.numero}")
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print(f"Piloto: {self.piloto.nome}")
        print(f"Total de assentos: {len(self.assentos)*len(self.assentos[0])}")

        # Calcula o total de assentos ocupados
        assentos_ocupados = 0
        for fila in self.assentos:
            for poltrona in fila:
                if poltrona.ocupado:
                    assentos_ocupados += 1

        print(f"Assentos ocupados: {assentos_ocupados}")