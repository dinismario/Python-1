#090  
from random import randint
v = 0
while True:
   print("=-="*20)
   print("VAMOS JOGAR PAR OU ÍMPAR")
   print("=-="*20)
   jogador = int(input("Digita um valor: ")) 
   computador = randint(0,10)
   total = jogador + computador
   tipo = " "
   while tipo not in  "PI":
      tipo = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
   print(f"Você jogou {jogador} e o computador {computador} , total é {total}")
   if tipo == "P":
      if total % 2 == 0 :
         print("Você Venceu!")
         v += 1
      else:
         print("Você Perdeu!")
         break 
      
   elif tipo == "I": 
      if total % 2 == 1 :
         print("Você Venceu!")
         v += 1
      else:
        print("Você Perdeu!")
        break 
      
   print("Vamos jogar novamente!")
print(f"GAME OVER! voce venceu {v} vezes ")
   
            