'''
Aplicação principal do nosso sistema de gerenciamento de vôos
'''

import os
from gerenciador_voo import GerenciadorVoo
from rich.console import Console
from rich.prompt import Prompt

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

    cria_piloto = gerenciador.cadastrar_comissario(nome, cpf, idade, matricula)                                                
    print(cria_piloto['msg'])   
    
    # Aguardar enter do usuário
    t = input("Pressione ENTER para continuar...")
    pass

def cadastrar_voo(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Vôos ✈️ ")
    numero = input("Digite o nome do comissário: ")  
    origem = input("Digite o CPF do comissário: ")
    destino = input("Digite a idade do comissário: ")    
    horario_partida = input("Digite a habilitacao do comissário: ") 
    duracao_estimada = input("Digite a habilitacao do comissário: ") 
    tarifa_basica = input("Digite a habilitacao do comissário: ") 
    piloto = input("Digite a habilitacao do comissário: ") 
    copiloto = input("Digite a habilitacao do comissário: ")
    comissarios_voo = input("Digite a habilitacao do comissário: ")        

                 
    cria_voo = gerenciador.cadastrar_voo(numero, origem, destino, horario_partida, duracao_estimada, tarifa_basica, piloto, copiloto, comissarios_voo)                                                
    print(cria_voo['msg'])               

def comprar_passagem():
    limpa_tela()
    exibe_titulo(" ✈️ Compra de Passagens ✈️ ")
    t = input()
    pass

def exibir_voo():
    limpa_tela()
    exibe_titulo(" ✈️ Informações de Vôo ✈️ ")
    t = input()
    pass

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