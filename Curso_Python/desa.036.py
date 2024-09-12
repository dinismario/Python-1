#036
def ficha(nome='desconhecido' ,golo=0):
    print(f'O Jogador {nome} fez {golo} gols no campeonato')

n = str(input("Digita o seu nome:"))
g = str(input("Digita o numero de gols: "))
if g.isnumeric():
    g = int(g)
else :
    g = 0

if n.strip()=='':
    ficha(golo=g)

else:
    ficha(n,g)            
