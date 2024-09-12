#Estrutura de repetição com For 

#for c in range(10,0,-1): #Este parametro faz o inverso ,-1 10 ate 1 , e este pula duas casas 0,7,2
  #  print(c)

#i = int(input("Ìnicio: "))
#f = int(input("Fim: "))
#p = int(input("Passa: "))
#for x in range(i,f+1,p):
 #   print(x)
#print("Fim")

soma = 0
for c in range(0,4):
    n= int(input("Digita um valor: "))
    soma += n # pode ser // soma = soma + n //
print("A soma entre essses valor é {}".format(soma))     
     