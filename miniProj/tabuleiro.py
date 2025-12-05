import json

def criarTabuleiro():
    global tabuleiro
    
    with open("tabuleiro.json", "r") as f:
        dados = json.load(f)
        
    comp = dados["comprimento"]
    larg = dados["largura"]
    
    tabuleiro = [["-" for c in range(comp)] for l in range(larg)]
    
    
    for linha in tabuleiro:
        print(" ".join(linha))
        
    input()

criarTabuleiro()

        