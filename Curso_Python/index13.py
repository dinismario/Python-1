#Fuções em python
#help(input)
#print(input.__doc__)

#docstrings

def contador(i,f,p):
    """
     #docstrings
    ->Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno  
    :Programa de Dinis Mário.
    """
    c = i
    while c <= f :
        print(f'{c}',end=" ")
        c += p
    print("FIM")    

contador(0,100,10)     