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

    cria_passageiro = gerenciador.cadastrar_passageiro(nome, cpf, idade)
    print(cria_passageiro['msg'])
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")

def cadastrar_piloto(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Pilotos ✈️ ")
    nome = input("Digite o nome do piloto: ")  
    cpf = input("Digite o CPF do piloto: ")
    idade = input("Digite a idade do piloto: ")
    matricula = input("Informar matricula:")  
    habilitacao = input("Digite a habilitacao do piloto: ") 

    cria_piloto = gerenciador.cadastrar_piloto(nome, cpf, idade, matricula, habilitacao)                                                
    print(cria_piloto['msg'])   
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")
    pass

def cadastrar_comissario(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Comissários ✈️ ")
    nome = input("Digite o nome do comissário: ")  
    cpf = input("Digite o CPF do comissário: ")
    idade = input("Digite a idade do comissário: ")    
    matricula = input("Digite a habilitacao do comissário: ") 
    idioma = input("Informar idioma: ")

    cria_piloto = gerenciador.cadastrar_comissario(nome, cpf, idade, matricula, idioma)                                                
    print(cria_piloto['msg'])   
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")
    pass

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
        gerenciador.lista_pilotos()
        cpf_copiloto_busca = input("Digite o cpf do copiloto a buscar: ") 
        copiloto = gerenciador.seleciona_piloto_por_cpf(cpf_piloto_busca)

        if copiloto not in gerenciador.lista_pilotos():
            print("Copiloto não localizado!")

        if cpf_copiloto_busca == piloto:
            print("O piloto e o copiloto não podem ser a mesma pessoa!")
            copiloto = None
        else:
            copiloto = cpf_copiloto_busca

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

        if opcao == '1':
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

def main():
    
    gerenciador = GerenciadorVoo()

    opcao_menu = ""
    while opcao_menu != '7':
        limpa_tela()
        exibe_menu()
        opcao_menu = Prompt.ask("[bold red]Digite a opção desejada: [/bold red]")
        verifica_opcao_menu(opcao_menu, gerenciador)
        
if __name__ == "__main__":
    main()