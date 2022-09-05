from piloto import Piloto

class GerenciadorVoo:
    '''
    Gerenciador de vôos, responsável por gerenciar vôos, reservas, 
    passagens, tripulação e tudo mais. 
    '''
    def __init__(self):
        self.passageiro=[]
        self.pilotos=[]
        self.comissarios=[]
        self.voos=[]

    def cadastrar_piloto(self, nome,cpf,idade,num_breve):
        p=Piloto(nome,cpf,idade,num_breve)
        self.pilotos.append(p)
        return True,"Piloto inserido com Sucesso"