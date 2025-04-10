# 🎯 Jogo de Adivinhação - Python

Um jogo simples em Python onde o jogador deve adivinhar um número aleatório entre 1 e 10.  
O jogador tem 3 vidas para tentar acertar o número sorteado.

---

## 🚀 Como funciona

- O programa sorteia um número aleatório entre 1 e 10.
- O jogador digita um número e recebe dicas se o número está acima ou abaixo do correto.
- O jogador tem 3 tentativas (vidas) por rodada.
- Ao acertar, ganha 1 ponto na pontuação.
- Ao errar todas as tentativas, o número correto é revelado.

---

## 📁 Estrutura do projeto

- O jogo é implementado dentro da classe `JogoAdivinhacao`.
- O método `jogar()` inicia uma rodada com número aleatório e controle de vidas.
- O número secreto é sorteado no início de cada partida e permanece o mesmo até o fim da rodada.

---

## 🧠 Exemplo de uso

```python
Digite seu nome: Alice
Digite um numero de 1 a 10: 7
Voce errou agora voce so tem 2 vidas
O numero aleatorio é menor que o numero que voce digitou
Digite um numero de 1 a 10: 4
Parabens voce acertou sua pontuacao agora é 1