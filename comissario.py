class Comissario():
    '''
    Classe para representar um comissário ou comissária de bordo
    '''
    def __init__(self,nome,cpf,idade,pcd,funcao):
        self.pcd = pcd
        self.nome =nome
        self.idade =idade
        self.cpf =cpf
        self.funcao = funcao

    def informacoes(self):
        return 'Nome: '+self.nome+',cpf: '+self.cpf+', Idade: '+self.idade+', PCD: '+self.pcd+', Funcao: '+self.funcao