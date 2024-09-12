#22
from random import randint

while True:
 computador = randint(1,10)
 jogador = int(input("Digita um valor entre (1-10): "))
 s = jogador + computador 
 print(f"O jogador jogou {jogador} e computador {computador } a soma é {s}")
 if s % 2 == 0:
  print("Este número é par ")
 else:
  print("Este número é ímpar!") 