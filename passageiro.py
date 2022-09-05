from pessoa import Pessoa
class Passageiro(Pessoa):
    '''
    Classe para representar um passageiro
    '''
    def __init__(self, assento, numeroVoo, horaVoo, empresaAerea):
      super().__init__(nome, cpf, sexo, pcd, telefone, dataNascimento, email, endereco)
      self.assento = assento
      self.numeroVoo = numeroVoo
      self.horaVoo = horaVoo
      self.empresaAerea = empresaAerea