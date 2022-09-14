

class Pessoa():
    '''
    Classe para representar uma pessoa
    '''
    def __init__(self, nome, cpf, idade, pcd):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.pcd = pcd

    def compara(self, outra_pessoa):
        if self.cpf == outra_pessoa.cpf:
            return True
        else:
            return False