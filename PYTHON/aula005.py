#Variáveis Compostas 
# os três tipos de variáveis Compostas são : listas ; tuplas ; dicionários.
# LISTAS (Array)

notas = [1, 2, 3, 4]
notas.append(11) #adicinar um elemento na lista
print(notas)

notas.remove(1) # Remover elementos na lista 
print(notas)

index = notas.index(3) # obtem o index de um valor 
print(index)

#Removendo o valor pelo Index 
notas.remove(notas[index])
print(notas)


# Atualizar valores pelo index
notas[0] = notas[0] + 5
print(notas)
