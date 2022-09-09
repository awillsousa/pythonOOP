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
    cpf = input("Digite o cpf do passageiro: ")
    idade = input("Digite o idade do passageiro: ")
    pcd = input("Informe se o passageiro é PCD: ")
    fidelidade = input("Digite o número do cartão fidelidade do passageiro: ")
    consulta = gerenciador.consultar_passageiro(cpf)
    if consulta[0]:
        print('Passageiro já está cadastrado com este CPF!')
        print(consulta[1])
    else:
        resultado = gerenciador.cadastrar_passageiro(nome,cpf,idade,pcd,fidelidade)
        if resultado[0]:
            print(resultado[1])
    t=input("Pressione ENTER para continuar")

def cadastrar_piloto(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Pilotos ✈️ ")
    nome = input("Digite o nome do piloto: ")
    cpf = input("Digite o cpf do piloto: ")
    idade = input("Digite o idade do piloto: ")
    num_breve = input("Digite o num_breve do piloto: ")
    consulta = gerenciador.consultar_piloto(num_breve)
    if consulta[0]:
        print('Piloto já está cadastrado com este Breve!')
        print(consulta[1])
    else:
        resultado = gerenciador.cadastrar_piloto(nome,cpf,idade,num_breve)
        if resultado[0]:
            print(resultado[1])
    t=input("Pressione ENTER para continuar")

def cadastrar_comissario(gerenciador):#nome,cpf,idade,pcd,funcao
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Comissários ✈️ ")
    nome = input("Digite o nome do comissario: ")
    cpf = input("Digite o cpf do comissario: ")
    idade = input("Digite o idade do comissario: ")
    pcd = input("Informe se o comissario é PCD: ")
    funcao = input("Digite a função do comissario: ")
    consulta = gerenciador.consultar_comissario(cpf)
    if consulta[0]:
        print('Comissário já está cadastrado com este CPF!')
        print(consulta[1])
    else:
        resultado = gerenciador.cadastrar_comissario(nome,cpf,idade,pcd,funcao)
        if resultado[0]:
            print(resultado[1])
    t=input("Pressione ENTER para continuar")

def cadastrar_voo():
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Vôos ✈️ ")
    t = input()
    pass

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

def verifica_opcao_menu(opcao,gerenciador):

        if opcao == '1':
            cadastrar_passageiro(gerenciador)
        elif opcao == '2':
            cadastrar_piloto(gerenciador)
        elif opcao == '3':
            cadastrar_comissario(gerenciador)
        elif opcao == '4':
            cadastrar_voo()
        elif opcao == '5':
            comprar_passagem()
        elif opcao == '6':
            exibir_voo()

def main():
    
    gerenciador = GerenciadorVoo()

    opcao_menu = ""
    while opcao_menu != '7':
        limpa_tela()
        exibe_menu()
        opcao_menu = Prompt.ask("[bold red]Digite a opção desejada: [/bold red]")
        verifica_opcao_menu(opcao_menu,gerenciador)

        

if __name__ == "__main__":
    main()