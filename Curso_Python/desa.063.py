#064
import random
listas = list ()
l = list()
for x in range(1,5):
    listas.append(str(input("Digita uma senha: ")))
    senhas = random.choices(listas)
    l.append(listas[:])
print(f"Entre todas senhas digitas : {listas} a senha escolhida é {senhas}")

  



