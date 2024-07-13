meu_dict = {
'Gabriel': 11630097,
'Paiva':  11630130,
'Felipe': 11630001
}

nome = input('digite um nome:')
cep = meu_dict.get(nome)

print(f'o cep de {nome} é {cep}') 