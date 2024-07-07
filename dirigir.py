idade = int(input('Qual a sua idade?'))
if idade > 18:
    print("individuo possui idade mínima pra dirigir")
elif idade == 17 or idade == 18:
    print("individuo ainda não está apto para dirigir")
else:
    print("individuo não possui idade mínima pra dirigir")