#110
from random import randint
from time import sleep
from operator import itemgetter

jogo = {"jogador1": randint(1, 6),
           "jogagor2": randint(1, 6),
           "jogador3": randint(1, 6),
           "jogador4": randint(1, 6)
          }
ranking = dict()
print("VALORES SORTEADOS: ")
for k , v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-=-"*20)
print("  ==RANKING==  ")
for i, v in enumerate(ranking):
    print(f"{i+1}ª lugar: {v[0]} com {v[1]}")
    sleep(1)
 
