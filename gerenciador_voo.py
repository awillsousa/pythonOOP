from comissario import Comissario
from passageiro import Passageiro
from piloto import Piloto
from voo import Voo

class GerenciadorVoo:
    '''
    Gerenciador de vôos, responsável por gerenciar vôos, reservas, 
    passagens, tripulação e tudo mais. 
    '''
    def __init__(self):
        self.passageiros = []
        self.pilotos = []
        self.comissarios = []
        self.voos = []

    def cadastrar_passageiro(self, nome, cpf, idade):      
        if self.passageiro_ja_existe(cpf):
            return {'resultado': False,
                'msg': 'Passageiro já cadastrado!'}
        else:
            p = Passageiro(nome, cpf, idade)      
            self.passageiros.append(p)

            return {'resultado': True,
                    'msg': 'Passageiro inserido com sucesso!'}
    
    def passageiro_ja_existe(self, cpf):        
        for p in self.passageiros:
            if p.cpf == cpf:
                return True

        return False

    def cadastrar_piloto(self, matricula, nome, cpf, idade, habilitacao):
        
        if self.piloto_ja_existe(cpf):
            return {'resultado': False,
                'msg': 'Piloto já cadastrado!'}
        else:
            p = Piloto(matricula, nome, cpf, idade, habilitacao)        
            self.pilotos.append(p)

            return {'resultado': True, 
                    'msg': 'Piloto inserido com sucesso!'}
        
    def piloto_ja_existe(self, cpf):        
        for p in self.pilotos:
            if p.cpf == cpf:
                return True

        return False
    
    def cadastrar_comissario(self, nome, cpf, idade, matricula, idioma):            
        if self.comissario_ja_existe(cpf):
            return {'resultado': False,
                'msg': 'Comissário já cadastrado!'}
        else:
            p = Comissario(nome, cpf, idade, matricula, idioma)       
            self.pilotos.append(p)

            return {'resultado': True,
                    'msg': 'Comissário inserido com sucesso!'}
        
    def comissario_ja_existe(self, cpf):        
        for p in self.pilotos:
            if p.cpf == cpf:
                return True

        return False