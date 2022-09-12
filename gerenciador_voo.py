from comissario import Comissario
from passageiro import Passageiro
from piloto import Piloto

class GerenciadorVoo:
    '''
    Gerenciador de vôos, responsável por gerenciar vôos, reservas, 
    passagens, tripulação e tudo mais. 
    '''
    def __init__(self):
        self.passageiros = []
        self.voos = []
        self.pilotos = []
        self.assentos = []


    def cadastrar_passageiro (self, nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte):
        if self.passageiro_ja_existe(cpf):
            return ('resultado':false)
            
        passageiro1 = Passageiro (nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte)
        self.passageiros.append (passageiro1)

    
    def cadastrar_piloto (self, nome, rg, cpf, idade, sexo, matricula, horas_de_voo, habilitacao, exame_medico):
    
        piloto1 = Passageiro (nome, rg, cpf, idade, sexo, matricula, horas_de_voo, habilitacao, exame_medico)
        self.pilotos.append (piloto1) 
    
    def cadastrar_comissario (self, nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte):
    
        comissario1 = Comissario (nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte)
        self.comissarios.append (comissario1) 