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

    def consultar_piloto(self,num_breve):
        for p in self.pilotos:
            if p.num_breve == num_breve:
                return True, p.informacoes()
        return False, 'Não cadastrado!'
        