#046
nome = str(input("Digita o seu nome completo: ")).strip()
print("O seu nome em maisculas é {}".format(nome.upper()))
print("O seu nome em minuscula é {}".format(nome.lower()))
print("O seu nome tem {} letras".format(len(nome) - nome.count(' ')))
#print("O seu primeiro nome tem {} letras".format(nome.find(' ')))
separa = nome.split()
print("O seu primeiro nome é {} e tem {} letras".format(separa[0],len(separa[0])))



