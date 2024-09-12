compras = ["Pão","Banana","Maçã","Pera","Ananas","Morango","Limão","Abacate","Manga","Cana"]
usuario = input("O que quer comprar?: ")

for prod in compras:
    if prod == usuario:
        print("Esta fruta faz parte da Lista!")
        break

    else:
        print("Não temos esta fruta!")
