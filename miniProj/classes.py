import colorama
from colorama import Fore, Style

# Inicializa Colorama
colorama.init(autoreset=True)

class NaveModelo:
    def __init__(self, nome, cor, perda_energia, simbolo):
        self.nome = nome
        self.cor = Fore.WHITE # Usar branco como default
        self.energia = 100
        self.perda_energia = perda_energia
        self.simbolo = simbolo

    def perder_energia(self):
        self.energia -= self.perda_energia
        if self.energia < 0:
            self.energia = 0

    def mostrar_status(self):
        print(f"{self.cor}Nave: {self.nome} | Energia: {self.energia} | Símbolo: {self.simbolo}{Style.RESET_ALL}")

class NaveFilha(NaveModelo):
    def __init__(self, nome, cor, perda_energia, simbolo, energia_extra):
        super().__init__(nome, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def mostrar_status(self):
        print(f"{self.cor}Nave: {self.nome} | Energia: {self.energia} | Energia Extra: {self.energia_extra} | Símbolo: {self.simbolo}{Style.RESET_ALL}")

# --------- NAVES ----------
nave1 = NaveFilha("Ágil", Fore.RED, 35, "A", 0)
nave2 = NaveFilha("Equilíbrio", Fore.BLUE, 25, "E", 25)
nave3 = NaveFilha("Tanque", Fore.GREEN, 20, "T", 40)

todasAsNaves = [nave1, nave2, nave3]

#nave1.mostrar_status()
#nave2.mostrar_status()
#nave3.mostrar_status()