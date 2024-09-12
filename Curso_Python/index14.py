#Módulo e pacotes 
def fatorial (n):
    f = 1 
    for c in range(1, n+1):
        f = f * c  
    return f 

num = int(input("Digita um valor: "))
fat = fatorial(num)
print(f'O fatorial {num} é {fat}')