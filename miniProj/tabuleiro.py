import os
import json
import random
from classes import todasAsNaves  # lista de objs

tabuleiro = []

def escolherNomeJogo():
    global tabuleiro
    pastaSaves = "./pastaSaves"
    
    # Verificar se a pasta existe
    os.makedirs(pastaSaves, exist_ok=True)
    
    print("\n  =================================\n")
    print("  Escreve o nome do jogo a guardar: ")
    nome = input("\n  =================================\n")
    nome = nome.lower()

    if nome + ".json" in os.listdir(pastaSaves):
        print("\n  ==========================================================\n")
        print("  Já existe um jogo guardado com esse nome. Escolhe outro...")
        print("\n  ==========================================================\n")
        escolherNomeJogo()
    else:
        criarTabuleiro(nome)

def criarTabuleiro(nomeFicheiro):
    global tabuleiro
    
    # Ler dimensões do ficheiro tabuleiro.json
    with open("tabuleiro.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        
    comp = dados["comprimento"]
    larg = dados["largura"]
    
    # Criar o tabuleiro global
    tabuleiro = [["-" for _ in range(comp)] for _ in range(larg)]
    
    # Guardar dimensões no JSON
    dados_guardar = {
        "tabuleiro": {
            "comprimento": comp,
            "largura": larg
        }
    }

    # Guardar o ficheiro JSON dentro da pasta saves/
    caminho_ficheiro = os.path.join("pastaSaves", nomeFicheiro + ".json")
    with open(caminho_ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados_guardar, f, ensure_ascii=False, indent=4)

def imprimirTabuleiro():
    global tabuleiro
    comp = len(tabuleiro[0])
    larg = len(tabuleiro)
    
    # Cabeçalho das colunas
    print("   ", end="")
    for i in range(comp):
        print(f"  {i} ", end="")
    print()
    
    # Linha superior do frame
    print("   " + "+---"*comp + "+")
    
    # Linhas do tabuleiro
    for y in range(larg):
        print(f"{chr(65+y)}  |", end="")
        for x in range(comp):
            print(f" {tabuleiro[y][x]} |", end="")
        print()
        print("   " + "+---"*comp + "+")

def imprimirTabuleiroComNaves():
    global tabuleiro
    comp = len(tabuleiro[0])
    larg = len(tabuleiro)
    
    # Cabeçalho das colunas
    print("   ", end="")
    for i in range(comp):
        print(f"  {i} ", end="")
    print()
    
    # Linha superior do frame
    print("   " + "+---"*comp + "+")
    
    # Linhas do tabuleiro
    for y in range(larg):
        print(f"{chr(65+y)}  |", end="")
        for x in range(comp):
            print(f" {tabuleiro[y][x]} |", end="")  # já inclui as naves
        print()
        print("   " + "+---"*comp + "+")

def colocarNaves(naves):
    global tabuleiro
    larg = len(tabuleiro)
    comp = len(tabuleiro[0])

    for nave in naves:
        while True:
            x = random.randint(0, comp - 1)
            y = random.randint(0, larg - 1)
            if tabuleiro[y][x] == "-":  # posição vazia
                tabuleiro[y][x] = nave.simbolo
                break

def colocarTiros(): 
    tiros = []  # lista para armazenar os tiros
    larg = len(tabuleiro)
    comp = len(tabuleiro[0])
    
    print("\nEscolhe 3 posições para disparar (ex: A0, B2, C3):")
    
    while len(tiros) < 3:
        entrada = input(f"Tiro {len(tiros)+1}: ").upper().strip()
        
        # Validar formato da entrada
        if len(entrada) < 2:
            print("Formato inválido. Exemplo válido: A0")
            continue
        
        linha = entrada[0]
        coluna = entrada[1:]
        
        if not linha.isalpha() or not coluna.isdigit():
            print("Formato inválido. Exemplo válido: A0")
            continue
        
        y = ord(linha) - 65  # converte letra para índice
        x = int(coluna)
        
        # Verificar se as coordenadas estão dentro do tabuleiro
        if y < 0 or y >= larg or x < 0 or x >= comp:
            print("Coordenadas fora do tabuleiro. Tente novamente.")
            continue
        
        # Verificar se o tiro já foi escolhido
        if (y, x) in tiros:
            print("Você já atirou nessa posição. Escolha outra.")
            continue
        
        # Adicionar o tiro à lista
        tiros.append((y, x))
    
    print("\nTiros escolhidos:", [(chr(y+65), x) for y, x in tiros])
    return tiros


# teste ------------------------------------------------

escolherNomeJogo()

# Colocar todas as naves importadas
colocarNaves(todasAsNaves)

# Mostrar o tabuleiro final com naves
imprimirTabuleiroComNaves()

input("Pressione Enter para sair...")
