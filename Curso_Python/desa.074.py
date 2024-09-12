#074

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1 ) * razao

for x in range(primeiro, decimo+razao,razao):
    print("{}".format(x),end=" -> ")
print("ACABOU!")