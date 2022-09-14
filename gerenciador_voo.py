from piloto import Piloto
from passageiro import Passageiro
from comissario import Comissario

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
        
    # Cadastrando passageiro
    
    def cadastrar_passageiro(self, nome, cpf, idade, pcd):
        if self.passageiro_ja_existe(cpf):
            return {'resultado': False, 'msg': 'Passageiro já cadastrado!'}
        else:
            p = Passageiro(nome, cpf, idade, pcd)
            self.passageiros.append(p)
            
            return {'resultado': True, 'msg': 'Passageiro inserido com sucesso!'}
    
    # Método para comparar CPF inserido com os que tem na lista
    def passageiro_ja_existe(self, cpf):
        for p in self.passageiros:
            if p.cpf == cpf:
                return True
        
        return False
    
    def seleciona_passageiro_por_cpf(self, cpf):
        for p in self.passageiros:
            if p.cpf == cpf:
                return p
        return p
    
    def lista_passageiros(self):
        print("\nPassageiros cadastrados no sistema")
        for p in self.passageiros:
            print(f"{p.nome} - CPF: {p.cpf}")
        print()


    # Cadastrar pilotos
    def cadastrar_piloto(self, nome, cpf, idade, num_breve):
        
        if self.piloto_ja_existe(cpf):
            return {'resultado': False, 
                'msg': 'Piloto já cadastrado!'}
        else:
            p = Piloto(nome, cpf, idade, num_breve)        
            self.pilotos.append(p)

            return {'resultado': True, 
                    'msg': 'Piloto inserido com sucesso!'}
        
    def piloto_ja_existe(self, cpf):
        
        for p in self.pilotos:
            if p.cpf == cpf:
                return True

        return False    
    
    # Cadastrar comissários
    def cadastrar_comissario(self, nome, cpf, idade, pcd=False):
        if self.comissario_ja_existe(cpf):
            return {'resultado': False,'msg': 'Comissário já cadastrado!'}
        else:
            p = Comissario(nome, cpf, idade, pcd)
            self.comissarios.append(p)

            return {'resultado': True, 'msg': 'Comissário inserido com sucesso!'}
        
    def comissario_ja_existe(self,cpf):
        for p in self.comissarios:
            if p.cpf == cpf:
                return True
        return False
        


        