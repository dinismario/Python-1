#109
import math
angulo = float(input("Digita um  ângulo: "))
seno = math.sin(math.radians(angulo))
cos  = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f"O angulo de {angulo} Seno é {seno:.2f}")
print(f"O ângulo de {angulo} Cosseno é {cos:.2f}")
print(f"O angulo de {angulo} Tangente é {tang:.2f}")
