#23
tuplas = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")

while True:
    for x in range(0,20):
     num = int(input("Digita um valor entre (0-20): "))
     print(f"Você digitou o número {num}")
     if num > 20:
         print("Tenta novamente.Digita um  números entre 0-20")

     elif num < 0 :
         print("Tenta novamente.Digita um  números entre 0-20")

   