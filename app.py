'''
Aplicação principal do nosso sistema de gerenciamento de vôos
'''

import os
from gerenciador_voo import GerenciadorVoo
from rich.console import Console
from rich.prompt import Prompt
from voo import Voo

console = Console()

def limpa_tela():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def exibe_titulo(texto):
    tamanho_titulo=33
    console.print(f"[bold cyan]{'='*tamanho_titulo}[/bold cyan]")
    console.print(texto.center(tamanho_titulo))
    console.print(f"[bold cyan]{'='*tamanho_titulo}[/bold cyan]")

def exibe_menu():
    
    exibe_titulo(" ✈️ VOANDO BAIXO LINHAS AÉREAS ✈️ ")
    texto_menu = '''
    1 - Cadastrar Passageiro
    2 - Cadastrar Piloto
    3 - Cadastrar Comissário
    4 - Cadastrar Vôo
    5 - Comprar Passagem
    6 - Exibir Vôo
    7 - Sair
    '''
    console.print(texto_menu)

def cadastrar_passageiro(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Passageiros ✈️ ")
    nome = input("Digite o nome do passageiro: ")
    cpf = input("Digite o CPF do passageiro: ")
    idade = input("Digite a idade do passageiro: ")
    
    # Indicação se o passageiro é PCD ou não
    pcd = input("O passageiro é PCD (S/N)?")
    while pcd not in ['S', 'N']:
        print("Opção inválida! Digite S ou N.")
        pcd = input("O passageiro é PCD (S/N)?")
    
    pcd = True if pcd == 'S' else False

    cria_passageiro = gerenciador.cadastra_passageiro(nome, cpf, idade, pcd)
    print(cria_passageiro['msg'])
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")
    
def cadastrar_piloto(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Pilotos ✈️ ")
    nome = input("Digite o nome do piloto: ")
    cpf = input("Digite o CPF do piloto: ")
    idade = input("Digite a idade do piloto: ")
    num_breve = input("Digite o num. do brevê do piloto: ")

    cria_piloto = gerenciador.cadastra_piloto(nome, cpf, idade, num_breve)
    print(cria_piloto['msg'])
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")

def cadastrar_comissario(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Comissários ✈️ ")

    # entrada de dados dos comissários (cadastro)
    nome = input("Digite o nome do comissário(a): ")
    cpf = input("Digite o CPF do comissário(a): ")
    idade = input("Digite a idade do comissário(a): ")
    pcd = input("O comissário(a) é PCD (S/N)? ")

    # chamada do gerenciador
    cria_comissario = gerenciador.cadastra_comissario(nome, cpf, idade, pcd)
    print(cria_comissario['msg'])

    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")
    
def cadastrar_voo(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Vôos ✈️ ")    
    numero  = input("Digite o número do voo: ") 
    origem = input("Digite a origem do voo: ") 
    destino = input("Digite o destino do voo: ") 
    horario_partida = input("Digite o horário de partida do voo: ") 
    duracao_estimada = input("Digite a duração estimada do voo: ") 
    tarifa_basica = input("Digite a tarifa básica do voo: ") 
    
    # lista os pilotos disponíveis
    gerenciador.lista_pilotos()

    # selecao do piloto
    piloto = None
    while piloto is None:
        cpf_piloto_busca = input("Digite o cpf do piloto a buscar: ") 
        piloto = gerenciador.seleciona_piloto_por_cpf(cpf_piloto_busca)
        if piloto is None:
            print("Piloto não localizado!")

    print(f"Piloto {piloto.nome} selecionado!")

    # selecao do copiloto
    copiloto = None
    while copiloto is None:
        cpf_copiloto_busca = input("Digite o cpf do copiloto a buscar: ") 
        copiloto = gerenciador.seleciona_piloto_por_cpf(cpf_copiloto_busca)

        if copiloto is None:
            print("Copiloto não localizado!")

        if copiloto.compara(piloto) == True:
            print("O piloto e o copiloto não podem ser a mesma pessoa!")
            copiloto = None

    print(f"Copiloto {copiloto.nome} selecionado!")

    # selecao dos comissarios    
    comissarios_voo = []
    comissario_selecionado = None
    inserir_novo_comissario = True

    while inserir_novo_comissario:
        gerenciador.lista_comissarios()
        while comissario_selecionado is None:
            cpf_comissario_busca = input("Digite o cpf do comissário a buscar: ") 
            comissario_selecionado = gerenciador.seleciona_comissario_por_cpf(cpf_comissario_busca)
        
        comissarios_voo.append(comissario_selecionado)
        
        inserir_outro = input("Deseja inserir outro comissário? (S/N)")
        while inserir_outro not in ['S', 'N']:
            print("Opção inválida! Digite S ou N.")
            inserir_outro = input("Deseja inserir outro comissário? (S/N)")
        
        if inserir_outro == 'S':
            inserir_novo_comissario = True
        else:
            inserir_novo_comissario = False
    
    # finalmente, cria o objeto da classe Voo
    v = gerenciador.cadastra_voo(numero, origem, destino, horario_partida, 
                                duracao_estimada, tarifa_basica, piloto, copiloto, 
                                comissarios_voo)
    
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")

def comprar_passagem(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Compra de Passagens ✈️ ")

    # Exibe a lista de passageiros
    gerenciador.lista_passageiros()

    # Seleciona o passageiro a ser vendida a passagem
    passageiro = None
    while passageiro is None:
        cpf_passageiro = input("Digite o cpf do passageiro: ") 
        passageiro = gerenciador.seleciona_passageiro_por_cpf(cpf_passageiro)
        if passageiro is None:
            print("Passageiro não localizado!")

    print(f"Passageiro {passageiro.nome} selecionado!") 

    # Exibe a lista de voos
    gerenciador.lista_voos()

    # Selecione o vôo
    voo = None
    while voo is None:
        num_voo = input("Digite o número do voo: ") 
        voo = gerenciador.seleciona_voo_por_numero(num_voo)
        if voo is None:
            print("Voo não localizado!")

    print(f"Voo {voo.numero} selecionado!") 

    # Exibe os assentos
    voo.exibe_assentos()
    
    # Seleciona o assento
    fila = int(input("Digite o número da fila: "))
    poltrona = int(input("Digite o número da poltrona: "))
    
    while not voo.assento_valido(fila-1, poltrona-1) or\
               voo.assento_ocupado(fila-1, poltrona-1):
        
        console.print(f"[bold red]\nAssento ocupado ou inválido!\n[/bold red]")      
        fila = int(input("Digite o número da fila: "))
        poltrona = int(input("Digite o número da poltrona: "))

    voo.ocupa_assento(fila-1, poltrona-1, passageiro)

    print(f"Passageiro {passageiro.nome} - Assento: fila {fila} poltrona {poltrona}")

    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")

def exibir_voo(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Informações de Vôo ✈️ ")

    # Exibe a lista de voos
    gerenciador.lista_voos()

    # Selecione o vôo
    voo = None
    while voo is None:
        num_voo = input("Digite o número do voo: ") 
        voo = gerenciador.seleciona_voo_por_numero(num_voo)
        if voo is None:
            print("Voo não localizado!")

    voo.exibe_informacoes()
    voo.exibe_assentos()

    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")

def verifica_opcao_menu(opcao, gerenciador):

        if  opcao == '1':
            cadastrar_passageiro(gerenciador)
        elif opcao == '2':
            cadastrar_piloto(gerenciador)
        elif opcao == '3':
            cadastrar_comissario(gerenciador)
        elif opcao == '4':
            cadastrar_voo(gerenciador)
        elif opcao == '5':
            comprar_passagem(gerenciador)
        elif opcao == '6':
            exibir_voo(gerenciador)

def cria_dados_teste(gerenciador):
    # passageiros
    gerenciador.cadastra_passageiro(nome='Jetty Chan', 
                                    cpf='876543098-99', 
                                    idade=41)
    gerenciador.cadastra_passageiro(nome='Arnold Xivarzinagar', 
                                    cpf='85458578-88', 
                                    idade=36)
    gerenciador.cadastra_passageiro(nome='Chuck Norrys', 
                                    cpf='214542177-21', 
                                    idade=24)
    gerenciador.cadastra_passageiro(nome='Jean-Claude Von Johnson', 
                                    cpf='323456543-76', 
                                    idade=55)
    gerenciador.cadastra_passageiro(nome='Johny Rambo', 
                                    cpf='454545777-56', 
                                    idade=36)
    # pilotos
    gerenciador.cadastra_piloto(nome='Flyng Man', 
                                             cpf='987789987-56', 
                                             idade=37, 
                                             num_breve='FR5678')
    gerenciador.cadastra_piloto(nome='Rubens Voandelo', 
                                             cpf='987712345-56', 
                                             idade=45, 
                                             num_breve='BR6699')                                             
    # comissarios
    gerenciador.cadastra_comissario(nome='Daniel Vais', 
                                    cpf='123321876-56', 
                                    idade=25)
    gerenciador.cadastra_comissario(nome='Muriel Fois', 
                                    cpf='321876123-44', 
                                    idade=31)
    gerenciador.cadastra_comissario(nome='Gediel Vens', 
                                    cpf='187632123-12', 
                                    idade=26)
    gerenciador.cadastra_comissario(nome='Etel Ficas', 
                                    cpf='4444555510-01', 
                                    idade=25,
                                    pcd=True)
    
    # voos
    p = gerenciador.seleciona_piloto_por_cpf('987789987-56')
    cp = gerenciador.seleciona_piloto_por_cpf('987712345-56')
 
    gerenciador.cadastra_voo(numero='AF3040', 
                            origem='SAO PAULO',  
                            destino='CURITIBA',  
                            horario_partida='10:00h', 
                            duracao_estimada='1h',  
                            tarifa_basica=500,  
                            piloto=p,  
                            copiloto=cp, 
                            comissarios_voo=gerenciador.comissarios[0:3])

    gerenciador.cadastra_voo(numero='PQ7788', 
                            origem='RIO GRANDE DO SUL',  
                            destino='ACRE',  
                            horario_partida='13:00h', 
                            duracao_estimada='10h',  
                            tarifa_basica=2500,  
                            piloto=p,  
                            copiloto=cp, 
                            comissarios_voo=gerenciador.comissarios[1:])

def main():
    
    gerenciador = GerenciadorVoo()

    # para fazer testes e não ter que digitar tudo
    # descomente a linha abaixo
    cria_dados_teste(gerenciador)

    opcao_menu = ""
    while opcao_menu != '7':
        limpa_tela()
        exibe_menu()
        opcao_menu = Prompt.ask("[bold red]Digite a opção desejada: [/bold red]")
        verifica_opcao_menu(opcao_menu, gerenciador)

if __name__ == "__main__":
    main()
