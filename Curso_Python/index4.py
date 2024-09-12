#Interropimentos do while
#Stop tem a função de parar o laço de repetição, ele desvia a execução do lado de fora da repetição "break".

#cont = 1
#while cont <= 10:
 #   print(cont," ", end="")
  #  cont += 1
#print("Fim")

n = s = 0
while True:
    n = int(input("Digita um valor:"))
    if n == 999:
        break
    
    s += n 
#print("A soma vale: {}".format(s))  
print(f"A soma vale: {s}")  #f string
  

