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
            pa = Passageiro(nome, cpf, idade)      
            self.passageiros.append(pa)

            return {'resultado': True,
                    'msg': 'Passageiro inserido com sucesso!'}
    
    def passageiro_ja_existe(self, cpf):        
        for pa in self.passageiros:
            if pa.cpf == cpf:
                return True

        return False

    def cadastrar_piloto(self, matricula, nome, cpf, idade, habilitacao):
        
        if self.piloto_ja_existe(cpf):
            return {'resultado': False,
                'msg': 'Piloto já cadastrado!'}
        else:
            pi = Piloto(matricula, nome, cpf, idade, habilitacao)        
            self.pilotos.append(pi)

            return {'resultado': True, 
                    'msg': 'Piloto inserido com sucesso!'}
        
    def piloto_ja_existe(self, cpf):        
        for pi in self.pilotos:
            if pi.cpf == cpf:
                return True

        return False
    
    def cadastrar_comissario(self, nome, cpf, idade, matricula, idioma):            
        if self.comissario_ja_existe(cpf):
            return {'resultado': False,
                'msg': 'Comissário já cadastrado!'}
        else:
            co = Comissario(nome, cpf, idade, matricula, idioma)       
            self.pilotos.append(co)

            return {'resultado': True,
                    'msg': 'Comissário inserido com sucesso!'}
        
    def comissario_ja_existe(self, cpf):        
        for co in self.pilotos:
            if co.cpf == cpf:
                return True

        return False