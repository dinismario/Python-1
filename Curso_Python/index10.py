#Listas dentro de listas 
#teste = list()
#teste.append("Dinis")
#teste.append(20)
#print(teste)

#galera = list()
#galera.append(teste[:])
#teste[0] = "Pedro"
#teste[1] = 22
#galera.append(teste)
#print(galera)

#galera = [['Dinis',20], ['Ana',8], ['Dilson',12], ['Helio',18]]
#for p in galera:
 #   print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmenor = 0

for i in range(0,3):
    dado.append(str(input('Digita o seu nome: ')))
    dado.append(int(input('Digita a sua idade: ')))
    galera.append(dado[:])  
    dado.clear()
    
print("---------------------------------")
for p in galera:
    if p[1]>=18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1

    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1   
print(f'Temos {totmai} maiores e {totmenor} menores de idades')
print("---------------------------------")

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
