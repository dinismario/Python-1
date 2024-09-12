def e_par(num):
    return num % 2 == 0

Lista = [1, 2, 3, 4, 5]

for n in Lista:
    
    if e_par(n):
        print(str(n) + " é par")

    else:
        print(str(n) + " é ímpar")
