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


    def cadastrar_passageiro (self, nome, rg, cpf, idade, sexo):
        if self.passageiro_ja_existe(cpf):
            return {'resultado': False, 
                'msg': 'Passageiro já cadastrado!'}
        else:
            p = Passageiro(nome, rg, cpf, idade, sexo)        
            self.passageiros.append(p)

            return {'resultado': True, 
                    'msg': 'Passageiro inserido com sucesso!'}
    
    def passageiro_ja_existe(self, cpf):        
        for p in self.passageiros:
            if p.cpf == cpf:
                return True

        return False 

    
    def cadastrar_comissario (self, tipo_de_voo, idioma, nome, rg, cpf, idade, sexo):
        if self.comissario_ja_existe(cpf):
            return {'resultado': False, 
                'msg': 'Comissario já cadastrado!'}
        else:
            p = Comissario(tipo_de_voo, idioma, nome, rg, cpf, idade, sexo)        
            self.comissarios.append(p)

            return {'resultado': True, 
                    'msg': 'Comissario inserido com sucesso!'}
    
    def comissario_ja_existe(self, cpf):        
        for p in self.comissario:
            if p.cpf == cpf:
                return True

        return False 

    def cadastrar_piloto (self, matricula, horas_de_voo, habilitacao, exame_medico, nome, rg, cpf, idade, sexo):
        if self.piloto_ja_existe(cpf):
            return {'resultado': False, 
                'msg': 'Piloto já cadastrado!'}
        else:
            p = Piloto(matricula, horas_de_voo, habilitacao, exame_medico, nome, rg, cpf, idade, sexo)        
            self.pilotos.append(p)

            return {'resultado': True, 
                    'msg': 'Piloto inserido com sucesso!'}
    
    def passageiro_ja_existe(self, cpf):        
        for p in self.pilotos:
            if p.cpf == cpf:
                return True

        return False 
