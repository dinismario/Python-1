#Continuação----
#brazil = list()
#estado1 = {'uf': 'Rio de janeiro', 'Sigla':'RJ'}
#estado2 = {'uf': 'São Paulo', 'Sigla':'SP'}

#brazil.append(estado1)
#brazil.append(estado2)
#print(brazil)
  
estado = dict()
brazil = list()

for c in range(0,3):
    estado['uf']= str(input("Unidade Federativa: "))
    estado['Sigla']= str(input("Sigla do estado: "))
    brazil.append(estado.copy())
    estado.clear()
for e in brazil:
    print(f'O seu estado {e}')
    