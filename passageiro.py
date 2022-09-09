class Passageiro():
    '''
    Classe para representar um passageiro
    '''
    def __init__(self,nome,cpf,idade,pcd,fidelidade=None):
        self.pcd = pcd
        self.nome =nome
        self.idade =idade
        self.cpf =cpf
        self.fidelidade = fidelidade

    def informacoes(self):
        return 'Nome: '+self.nome+',cpf: '+self.cpf+', Idade: '+self.idade+', PCD: '+self.pcd+', Fidelidade: '+self.fidelidade