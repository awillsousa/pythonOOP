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

def cadastrar_passageiro(bagagem, identificador_voo, passaporte, horas_de_voo, habilitacao, exame_medico, nome, rg, cpf, idade, sexo):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Passageiros ✈️ ")
    
    cria_passageiro = GerenciadorVoo.cadastrar_passageiro
    horas_de_voo = input("Informar horas de voo:")
    habilitacao = input("Informar horas de voo:")
    exame_medico = input("Informar horas de voo:")
    nome = input("Informar horas de voo:")
    rg = input("Informar horas de voo:")
    cpf = input("Informar horas de voo:")
    idade = input("Informar horas de voo:")
    sexo = input("Informar horas de voo:")
    print(cria_passageiro['msg'])
    t = input()
    pass

def cadastrar_piloto(matricula, horas_de_voo, habilitacao, exame_medico):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Pilotos ✈️ ")
    t = input()
    pass

def cadastrar_comissario(tipo_de_voo, idioma):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Comissários ✈️ ")
    t = input()
    pass

def cadastrar_voo(horario, identificador_aeronave):
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

def verifica_opcao_menu(opcao):

        if opcao == '1':
            cadastrar_passageiro()
        elif opcao == '2':
            cadastrar_piloto()
        elif opcao == '3':
            cadastrar_comissario()
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
        verifica_opcao_menu(opcao_menu)

        

if __name__ == "__main__":
    main()