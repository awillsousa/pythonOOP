from pessoa import Pessoa
class Piloto(Pessoa):
    '''
    Classe para representar piloto de vôo aéreo
    '''
    def __init__(self,nome,cpf,idade,num_breve):
        self.pcd = False
        self.nome =nome
        self.idade =idade
        self.cpf =cpf
        self.num_breve = num_breve

    def informacoes(self):
        return 'Nome: '+self.nome+',cpf: '+self.cpf+', Idade: '+self.idade+', Num. do Breve: '+self.num_breve
        
        
