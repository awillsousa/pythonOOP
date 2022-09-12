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
    
    nome = input("Informar o nome:")
    rg = input("Informar rg:")
    cpf = input("Informar cpf:")
    idade = input("Informar idade:")
    bagagem = input("Possui bagagem: S ou N:")
    identificador_voo  = input("Insira o identificador do voo: ")
    passaporte = input("Insira número do passaporte:")
  
    cria_passageiro = GerenciadorVoo.cadastrar_passageiro(nome, rg, cpf, idade, bagagem, identificador_voo, passaporte)
    print(cria_passageiro['msg'])

    t = input()

def cadastrar_piloto(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Pilotos ✈️ ")
    
    nome = input("Informar o nome:")
    rg = input("Informar rg:")
    cpf = input("Informar cpf:")
    idade = input("Informar idade:")
    matricula = input("Informar número de matrícula:")
    horas_de_voo = input("Informar horas de voo:")
    habilitacao = input("Informar número de habilitação:")
    exame_medico = input("informe se vigente exame médico S ou N:")
    
    cria_piloto = GerenciadorVoo.cadastrar_piloto(matricula, horas_de_voo, habilitacao, exame_medico, nome, rg, cpf, idade)
    print(cria_piloto['msg'])
    t = input()
    pass

def cadastrar_comissario(gerenciador):
    limpa_tela()
    exibe_titulo(" ✈️ Cadastro de Comissários ✈️ ")

    nome = input("Informar o nome:")
    rg = input("Informar rg:")
    cpf = input("Informar cpf:")
    idade = input("Informar idade:")
    sexo = input("Informar sexo:")
    tipo_de_voo = input("Informar o tipo de voo:")
    idioma = input("Informar o idioma:")

    cria_comissario = GerenciadorVoo.cadastrar_comissario(tipo_de_voo, idioma, nome, rg, cpf, idade)
    print(cria_comissario['msg'])

    t = input()
    pass

def cadastrar_voo(gerenciador):
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
        verifica_opcao_menu(opcao_menu)

        

if __name__ == "__main__":
    main()