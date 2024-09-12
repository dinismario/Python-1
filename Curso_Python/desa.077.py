#077
totmaior = 0
totmenor = 0
for x in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(x)))
    if x == 1:
        totmaior = peso
        totmenor = peso

    else:
        if peso > totmaior:
            totmaior = peso

        if peso < totmenor:
            totmenor = peso


print("O maior peso é {}Kg ".format(totmaior))        
print("O menor peso é {}Kg".format(totmenor)) 
        

