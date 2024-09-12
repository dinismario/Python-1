#029
alunos = list()
nota1 = nota2 = list()
media = 0

for i in range(0,3):
    alunos.append(str(input('Digita os seu nome: ')))
    nota1.append(int(input('Digita a sua nota 1: ')))
    nota2.append(int(input('Digita a sua nota 2: ')))
    alunos.append(nota1[:])
    alunos.append(nota2[:])

    nota1.clear()
    nota2.clear()


for x in alunos:
   media = (nota1+ nota2)/2
   print(f'A sua media é {media}!')