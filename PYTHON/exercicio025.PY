#Crie um programa que receba 5 nomes utilizando uma lista e a estrutura de repetição for , e imprima estes 5 numeros..

nomes = []
for x in range(5):
    nome= input("Digita o seu nome: ")
    nomes.append(nome)
for x in range(5):
    print(nomes[x])

