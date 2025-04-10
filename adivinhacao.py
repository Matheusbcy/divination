import random

class JogoAdivinhacao:
    def __init__(self, nome):
        self.nome = nome
        self.numero = 0
        self.pontuacao = 0

    def jogar(self):
        self.vidas = 3
        numero_aleatorio = random.randint(1, 10)
        while self.vidas > 0:
            self.numero = int(input("Digite um numero de 1 a 10: "))
            if numero_aleatorio == self.numero:
                self.pontuacao += 1
                print(f"Parabens voce acertou sua pontuacao agora é {self.pontuacao}")
                break
            else:
                self.vidas -= 1
                print(f"Voce errou agora voce so tem {self.vidas} vidas")
                if numero_aleatorio < self.numero and self.vidas >= 1:
                    print("O numero aleatorio é menor que o numero que voce digitou")
                elif numero_aleatorio > self.numero and self.vidas >= 1:
                    print("O numero aleatorio e maior que o numero que voce digitou")
        if self.vidas == 0:
            print(
                f"O numero gerado foi {numero_aleatorio}. infelizmentre voce perdeu, tente novamente!"
            )

nome = input("Digite seu nome: ")
jogador1 = JogoAdivinhacao(nome)
