#Desafio 005
nascim = int(input("Digita o seu ano de nascimento: "))
ano_atual = 2024
ano = str(ano_atual-nascim)

if nascim == 2015:
    print("Você tem {} anos: MIRIM ".format(ano_atual-nascim))

elif nascim == 2010:
    print("Você tem {} anos: INFANTIL".format(ano_atual-nascim))

elif nascim == 2005:
    print("Você tem {} anos: JUNIOR".format(ano_atual-nascim))   

elif nascim == 2004:
    print("Você tem {} anos: SENIOR".format(ano_atual-nascim))

elif nascim == 2000 or ano == 2003 or ano == 2002 or ano == 2001:
    print("Você tem {} anos: MASTER".format(ano_atual-nascim))    



