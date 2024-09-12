#valores = list()
#for cont in range(0,5):
#    valores.append(int(input("Digita um valor: ")))

#for c, v in enumerate(valores):
 #       print(f"Na posição {c} encontrei o valor {v}!")

a = [2,4,5,6]
b = a[:] 
b[2] = 7
print(f"lista A: {a}")
print(f"lista B: {b}")
