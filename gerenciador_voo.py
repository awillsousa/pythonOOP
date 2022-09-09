from piloto import Piloto

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



        