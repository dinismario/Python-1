#076
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for x in range(1, 8):
    nas = int(input("Em que ano a {}ª pessoa nasceu?: ".format(x)))
    idade = atual - nas
    if idade >= 21 :
        totmaior += 1
    else:
        totmenor +=1

print("Ao todo tivemos {} maior de idade ".format(totmaior))        
print("Ao todo tivemos {} menores de idade ".format(totmenor))