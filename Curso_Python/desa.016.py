#016
from random import randint
print(" 'Computador' Pensei em um número entre 0 á 10")
computador = randint(0,10)
acertou = False
while not acertou :
  jogador = int(input("Tenta adiviar:  "))
  if jogador == computador:
    acertou = True
    print(f"O computador pensou no número {computador} e jogador também {jogador}")
print("O jogador Acerou!")          