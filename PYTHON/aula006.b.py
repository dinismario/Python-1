#Estrutura de Repetição ou LOOP ...
#while , for 

#FOR:ele é usado qaundo o valores literaveis como listas , tuplas , dicionários.
#numeros = [1,2,3,4,5,6,6,7,8,9,10,"dinis"]

#for num in numeros:
 #   print(num)


#range:é uma fução que retorna um dado, ele só recebe números inteiros.
#for x in range(5) :
#   print(x)

num = int(input("Digita um valor: "))
for x in range(1, 13):
    # 2 x 1 = 2
    print(str(num) + " x " + str(x) + " = " + str(num * x)) 



