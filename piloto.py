from pessoa import Pessoa
class Piloto(Pessoa):
    '''
    Classe para representar piloto de vôo aéreo
    '''
    def __init__(self, registro, matricula, empresa, tipoAeronave):
        super().__init__(nome, cpf, sexo, pcd, telefone, dataNascimento, email, endereco)
        
        self.registro = registro
        self.matricula = matricula
        self.empresa = empresa
        self.tipoAeronave = tipoAeronave
        
        
        
piloto1 = Piloto(registro=789456123, matricula=456123456, empresa='tralala', tipoAeronavenome='Biturbo', nome='ze', cpf=78945612345, sexo='M', pcd=False, telefone='8859862355', dataNascimento='31/12/1991', email='ze@mail.com', endereco='logo ali')

piloto1.exibe_informacoes()
