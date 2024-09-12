#Dicionários {}...
#no dicionário para remover dados é o del, o values() ele retorna os dados do dicionario keys() ele retorna as chaves , items() ele retorna todo o valor do dicionário.
pessoas = {'Nome': 'Dinis', 'Sexo': 'M', 'Idade': '15'}
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
#print(pessoas.values())
#print(pessoas.keys())
#print(pessoas.items())
pessoas['Nome'] = 'edi '
pessoas ['peso'] = 20.2
for k , v in pessoas.items():
    print(f'{k} = {v}') 




