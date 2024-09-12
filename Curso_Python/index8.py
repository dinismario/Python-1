#Listas[] em python
#Elas tem algumas funções que são: append, remove, atualizar, index, del, pop.
#podemos declarar uma lista com um range : valor =list(4,11).
#sorted(reverse=True) este é para tornar a lista não organizada.


num = ["3","1","2","4","5","7"]
num[3] = 20
num.append(30)
num.insert(1,8)
num.pop(2)
#num.clear()
#num.remove(2)
if 7 in num:
    num.remove(7)
else:
    print("Não esta na lista!")
#num.sort(reverse=True)
print(num)
print(f"Esta lisatas tem {len(num)} elementos.")
