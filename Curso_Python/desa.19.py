#- Adivinhe o Número (usuário): Inverta o papel e faça o usuário adivinhar o número escolhido pelo computador
from random import randint

computador = int(input("Digita um valor entre 0 a 5: "))
jogador = randint(1,5)
acertou = False
while not acertou:
   computador = int(input(("Digita um valor: ")))
   if computador == jogador:
        acertou = True
print("Computador acertou o numero {} e jogador {}".format(computador, jogador))        
