#089
print("TABUADA DOS VALORES")

while True:
    num = int(input("Quer ver a tabuada de que valor?: "))
    print("-="*10)
    if num < 0:
        break
    print("-="*10)
    for x in range(1,13):
        print(f"{num} x {x} = {num*x}")
    print("-="*10)
print("Não é permitido números negativos!")