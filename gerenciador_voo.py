from passageiro import Passageiro


class GerenciadorVoo:
    '''
    Gerenciador de vôos, responsável por gerenciar vôos, reservas, 
    passagens, tripulação e tudo mais. 
    '''
    def __init__(self):
        self.passageiros = []

    def cadastrar_passageiro (self, nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte):
    
        passageiro1 = Passageiro (nome, rg, cpf, idade, sexo, bagagem, identificador_voo, passaporte)
        self.passageiros.append (passageiro1) 
    