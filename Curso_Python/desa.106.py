#106
palavras = {"aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar","praticar","trabalhar", "mercado", "programar", "futuro"}
print("VOGAIS NAS PALAVRAS:")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ",end="")
    for letra in p :
        if letra.lower() in "aeiou":
            print(letra,end=" ")