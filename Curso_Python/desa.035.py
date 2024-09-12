#035
def fatorial(n = 0):
    f = 1
    for c in range(n , 0 ,-1):
        f += c
    return f  

num = int(input("Digita um valor: "))
print(f'O fatorial deste valor {num} é igual a {fatorial(num)}')