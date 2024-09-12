#Tuplas são imótaveis(não mudam!),

#Tuplas()
#Listas[]
#Dicionario{}

#[1:] ele indica do 1 ate ao ultimo elemento
#[-1]  ele indica o ultimo elemento
# len() ele mostra a quantidade de elemeto.
#enumerate(),range()

lanche = ("Hambuguer","Suco","Pizza","Pudim")
#print(lanche)
#print(len(lanche))
#for comida in lanche:
#    print(f"Eu comi {comida}")
#print("Estou satisfeito!")   


#for cont in range(0, len(lanche)):
 #   print(lanche[cont])


for pos,comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicão {pos}")




