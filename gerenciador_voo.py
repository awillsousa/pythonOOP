from piloto import Piloto
from passageiro import Passageiro
from comissario import Comissario

class GerenciadorVoo:
    '''
    Gerenciador de vôos, responsável por gerenciar vôos, reservas, 
    passagens, tripulação e tudo mais. 
    '''
    def __init__(self):
        self.passageiros=[]
        self.pilotos=[]
        self.comissarios=[]
        self.voos=[]

    def cadastrar_piloto(self, nome,cpf,idade,num_breve):
        p=Piloto(nome,cpf,idade,num_breve)
        self.pilotos.append(p)
        return True,"Piloto inserido com Sucesso"

    def consultar_piloto(self,num_breve):
        for p in self.pilotos:
            if p.num_breve == num_breve:
                return True, p.informacoes()
        return False, 'Não cadastrado!'

    def cadastrar_passageiro(self, nome,cpf,idade,pcd,fidelidade):
        p=Passageiro(nome,cpf,idade,pcd,fidelidade)
        self.passageiros.append(p)
        return True,"Passageiro inserido com Sucesso"

    def consultar_passageiro(self,cpf):
        for p in self.passageiros:
            if p.cpf == cpf:
                return True, p.informacoes()
        return False, 'Não cadastrado!'


    def cadastrar_comissario(self,nome,cpf,idade,pcd,funcao):
        p=Comissario(nome,cpf,idade,pcd,funcao)
        self.comissarios.append(p)
        return True,"Comissario inserido com Sucesso"

    def consultar_comissario(self,cpf):
        for p in self.comissarios:
            if p.cpf == cpf:
                return True, p.informacoes()
        return False, 'Não cadastrado!'