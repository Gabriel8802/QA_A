dados = {
    "Recife": ['mateus', 'joao' , 'joaquim',],
    "Salvador": ['maria','michele','sabrina'],
    "São Paulo": ['jotta','joel','francisco'],
    "Manaus": ['dudu','leticia','mendes']
}

moradores_recife = dados.get("Recife", 0)
print(f"Moradores do Recife: {moradores_recife}")

