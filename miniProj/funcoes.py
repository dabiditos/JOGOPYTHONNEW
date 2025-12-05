import os, json

def capa():
    
    print("\n")
    
    print(" ----------------------------------------------------------\n")
    
    print(" |  ░█▀▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀▀    ░█  ░█ ░█▀▀█ ░█▀▀█  |")
    print(" |   ▀▀▀▄▄ ░█▄▄█ ░█▄▄█ ░█    ░█▀▀▀    ░█░█░█ ░█▄▄█ ░█▄▄▀  |")
    print(" |  ░█▄▄▄█ ░█    ░█ ░█ ░█▄▄█ ░█▄▄▄    ░█▄▀▄█ ░█ ░█ ░█ ░█  |\n")
    
    print(" ----------------------------------------------------------\n")
    
    print("\n  =============================\n")
    print("  Clica ENTER para começar.")
    input("\n  =============================\n\n  ")
    return ""

def menu():

    os.system("cls")
    print("\n  =============================")
    print("\n  1 - Iniciar Jogo")
    print("\n  2 - Carregar Jogo")
    print("\n  3 - Guardar Jogo")
    print("\n  4 - Configuração do tabuleiro")
    print("\n  5 - Sair")
    print("\n  =============================\n")

    print("  Escolhe uma opção: ")
    
    escolha = input("\n  =============================\n\n  ")

    if escolha == "1":
        os.system("cls")
        # funcao para iniciar
        
    elif escolha == "2":
        os.system("cls")
        # funcao para carregar
        
    elif escolha == "3":
        os.system("cls")
        # funcao para guardar
        
    elif escolha == "4":
        os.system("cls")
        # funcao para ver/alterar as dimensoes do tabuleiro
        tabuleiroInfo()
        # SE JA TIVER UM JOGO GUARDADO, O JOGO DEVE RESPEITAR AS
        # DIMENSOES DO JOGO GUARDADO E NAO DO QUE ESTA NO MENU
        # MAS TAMBEM DEVE GUARDAR OS DADOS QUE FICARAM NO MENU
    
    elif escolha == "5":
        os.system("cls")
        print("  A sair do jogo... Até breve!")
    else:
        os.system("cls")
        print("  Opção inválida, tenta novamente.\n\n")
        menu()
        
    return ""

def tabuleiroInfo():
    
    with open("tabuleiro.json", "r") as f:
        dados = json.load(f)
        
    comp = dados["comprimento"]
    larg = dados["largura"]
    
    print("\n  ==========================================")
    
    print("\n  Dimensões atuais do tabuleiro:\n")
    print(f"  Comprimento: {comp}\n")
    print(f"  Largura: {larg}\n")
    
    print("  ==========================================")

    print("\n  Desejas alterar as dimensões do tabuleiro?")
    
    print("\n  1 - Sim")
    print("\n  2 - Não")
    
    escolha = input("\n  ==========================================\n\n  ")
    
    if escolha == "1":
        os.system("cls")
        alterarTabuleiro()
        
    elif escolha == "2":
        os.system("cls")
        menu()
    else:
        os.system("cls")
        print("  Opção inválida, tenta novamente.\n\n")
        tabuleiroInfo()
        
    return ""

def alterarTabuleiro():
    os.system("cls")
    print("\n  =============================\n")

    print("  Escolhe o comprimento (2-10):")
    
    newComp = int(input("\n  =============================\n\n  "))
    if newComp > 10:
        newComp = 10
        print("\n  =======================================================\n")
        print("  Número maior que o valor máximo. Comprimento novo = 10.")
        print("\n  Clica ENTER para continuar.")
        input("\n  =======================================================\n\n  ")
    
    if newComp < 2:
        newComp = 2
        print("\n  =======================================================\n")
        print("  Número menor que o valor mínimo. Comprimento nova = 2.")
        print("\n  Clica ENTER para continuar.")
        input("\n  =======================================================\n\n  ")
    
    os.system("cls")
    
    print("\n  =============================\n")

    print("  Escolhe a largura (2-10):")
    
    newLarg = int(input("\n  =============================\n\n  "))
    
    if newLarg > 10:
        newLarg = 10
        os.system("cls")
        print("\n  ===================================================\n")
        print("  Número maior que o valor máximo. Largura nova = 10.")
        print("\n  Clica ENTER para continuar.")
        input("\n  ===================================================\n\n  ")
        
    
    if newLarg < 2:
        newLarg = 2
        print("\n  ==================================================\n")
        print("  Número menor que o valor mínimo. Largura nova = 2.")
        print("\n  Clica ENTER para continuar.")
        input("\n  ==================================================\n\n  ")
    
    # Abrir o ficheiro e ler os dados
    with open("tabuleiro.json", "r") as f:
        dados = json.load(f)

    # Substituir os valores existentes
    dados["comprimento"] = newComp
    dados["largura"] = newLarg

    # Guardar de volta no ficheiro
    with open("tabuleiro.json", "w") as f:
        json.dump(dados, f, indent=4)
        
    os.system("cls")

    print("\n  =============================\n")
    print("  Valores do tabuleiro atualizados com sucesso!\n")
    print("  Clica ENTER para voltar ao menu.")
    input("\n  =============================\n\n  ")
    
    menu()
    
    
    
        
# -- TESTES --

print(capa())
menu()
