#Loop de Repetição While....

#for x in range(1,10):
 #   print(x)

#c = 1 
#while c < 10:
 #   print(c)
  #  c = c+1 
#print("FIM")

#n = 1
#while n != 0:
 #   n = int(input("Digita um valor: "))
#print("Fim")    

#r = "S"
#while r == "S":
  #  n = int(input("Digita um valor:"))
   # r = str(input("Quer continuar? [S/N]"))
#print("FIM")

n = 1 
par = impar = 0

while n != 0:
    n = int(input("Digita um valor: "))
    if n != 0:
        if n % 2 == 0:
          par =+ 1
        else:  
          impar =+ 1
print("Você digitou {} numeros pares e {} numeros impares!".format(par, impar))      
      
print("FIM")
  



