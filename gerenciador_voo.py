from piloto import Piloto
from passageiro import Passageiro
from comissario import Comissario
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

    def cadastra_voo(self, numero, origem, destino, horario_partida, 
                        duracao_estimada, tarifa_basica, piloto, copiloto, 
                        comissarios_voo):
        if self.voo_ja_existe(numero):
            return {'resultado': False, 
                'msg': 'Voo já cadastrado!'}
        else:
            v = Voo(numero, origem, destino, horario_partida, 
            duracao_estimada, tarifa_basica, piloto, copiloto, 
            comissarios_voo)      
            self.voos.append(v)

            return {'resultado': True, 
                    'msg': 'Voo inserido com sucesso!'}

    def lista_voos(self):
        print("\nVoos cadastrados no sistema")
        for v in self.voos:
            print(f"{v.numero} - Origem: {v.origem} Destino: {v.destino}")
        print()

    def seleciona_voo_por_numero(self, numero):
        for v in self.voos:
            if v.numero == numero:
                return v
    
        return None

    def voo_ja_existe(self, numero):
        if self.seleciona_voo_por_numero(numero) is None:
            return False
        
        return True

    def lista_pilotos(self):
        print("\nPilotos cadastrados no sistema")
        for p in self.pilotos:
            print(f"{p.nome} - CPF: {p.cpf}")
        print()

    def seleciona_piloto_por_cpf(self, cpf):
        for p in self.pilotos:
            if p.cpf == cpf:
                return p
        
        return None

    def cadastra_piloto(self, nome, cpf, idade, num_breve):
        
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

    def seleciona_comissario(self):
        # exibir a lista de comissários
        print("\nComissários cadastrados no sistema")
        for i, c in enumerate(self.comissarios):
            print(f"{i+1} - {c.nome} [CPF:{c.cpf}]")
        
        # pede ao usuário que escolha um comissário
        numero_valido = False
        opcao_comissario = 0
        while not numero_valido:
            opcao_comissario = input("\nDigite o número do comissário na lista a escolher: ")
            opcao_comissario = int(opcao_comissario)

            if len(self.pilotos) >= opcao_comissario >= 1:
                numero_valido = True

        # recuperar o objeto piloto da lista de pilotos
        return self.comissarios[opcao_comissario-1]

    def lista_comissarios(self):
        print("\nComissários cadastrados no sistema")
        for c in self.comissarios:
            print(f"{c.nome} - CPF: {c.cpf}")
        print()

    def cadastra_comissario(self, nome, cpf, idade, pcd=False):
        if self.comissario_ja_existe(cpf):
            return {'resultado': False, 
                'msg': 'Comissário já cadastrado!'}
        else:
            p = Comissario(nome, cpf, idade, pcd)        
            self.comissarios.append(p)

            return {'resultado': True, 
                    'msg': 'Comissário inserido com sucesso!'}
    
    def comissario_ja_existe(self, cpf):        
        for p in self.comissarios:
            if p.cpf == cpf:
                return True

        return False  

    def cadastra_passageiro(self, nome, cpf, idade, pcd=False):
        if self.passageiro_ja_existe(cpf):
            return {'resultado': False, 
                'msg': 'Passageiro já cadastrado!'}
        else:
            p = Passageiro(nome, cpf, idade, pcd)        
            self.passageiros.append(p)

            return {'resultado': True, 
                    'msg': 'Passageiro inserido com sucesso!'}
    
    def seleciona_passageiro_por_cpf(self, cpf):
        for p in self.passageiros:
            if p.cpf == cpf:
                return p
        
        return None

    def passageiro_ja_existe(self, cpf):   
        for p in self.passageiros:
            if p.cpf == cpf:
                return True

        return False  

    def lista_passageiros(self):
        print("\nPassageiros cadastrados no sistema")
        for p in self.passageiros:
            print(f"{p.nome} - CPF: {p.cpf}")
        print()

        