class Assento():
    '''
    Classe para representar um assento
    '''

    def __init__(self, valor_tarifa):
      self.valor_tarifa = valor_tarifa
      self.ocupado = False
      self.passageiro = None

    def ocupa_assento(self, passageiro):
      self.passageiro = passageiro
      
    def desocupa_assento(self):
      self.passageiro = None

class AssentoBasico(Assento):
    '''
    Classe para representar um assento geral
    '''

    def __init__(self, valor_tarifa, desconto=0.0):
      
      super().__init__(valor_tarifa)      
      self.desconto = desconto
      self.tipo = "BASICO"

    def preco_final(self):
      return self.valor_tarifa - (self.valor_tarifa*self.desconto/100)

    def tipo(self):
      return self.tipo
    
class AssentoEmergencia(AssentoBasico):
    '''
    Classe para representar um assento espei
    '''

    def __init__(self, valor_tarifa, desconto=10):
      super().__init__(valor_tarifa)
      self.tipo = "EMERGENCIA"
      self.desconto = desconto
      
    def preco_final(self):
      return self.valor_tarifa - (self.valor_tarifa*self.desconto/100)


class AssentoConfort(AssentoBasico):
    '''
    Classe para representar um assento espei
    '''

    def __init__(self, valor_tarifa, extra, desconto=0.0):
      super().__init__(valor_tarifa)
      self.tipo = "CONFORT"
      self.desconto = desconto
      self.extra = extra

    def preco_final(self):
      return self.valor_tarifa - (self.valor_tarifa*self.desconto/100) + self.extra

  
class AssentoReservado(AssentoBasico):
    '''
    Classe para representar um assento reservado
    '''

    def __init__(self, valor_tarifa):
      super().__init__(valor_tarifa)
      self.tipo = "RESERVADO"
