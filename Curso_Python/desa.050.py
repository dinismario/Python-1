#050
nome = str(input("Digita uma frase: ")).upper()

print(" A letra A aparece {} na frase.".format(nome.count("A")))
print("A primeira A esta na posição {}".format(nome.find("A")))
print("A ultima letra A esta na posição {}".format(nome.rfind("A")))
print("".format(len(nome) - nome.count(" ")))




