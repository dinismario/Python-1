#exercício_015

genero = str(input("Digita o sue sexo [Mm/Ff]: "))
while genero not in "MmFf":
    genero = str(input("Dados Inválidos por favor digita novamente: "))
print("Sexo {} registrado com sucesso!".format(genero)) 


   
