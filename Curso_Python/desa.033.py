#033

#def fatorial(num = 1):
   # f = 1
   # for c in range(num , 0 , -1):
    #    f += c
   # return f
#n = int(input("Digita um valor: "))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input("Digita um valor: "))
print(par(num))    
if par(num):
    print("è par")

else:
    print("è ímpar")