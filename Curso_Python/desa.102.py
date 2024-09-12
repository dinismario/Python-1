#0102
valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valor)

for x in valor: 
    if x % 2 == 0:
        print("Par",end=" ")
        print(x)
    else:
        print("Impar",end=" ")
        print(x)