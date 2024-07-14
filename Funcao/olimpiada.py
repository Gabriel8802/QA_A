def alunos(numero):
    if numero % 2 == 0:
        print('você é do time azul')
    else:
        print('você é do time amarelo')

while True:
    n1=int(input('digite um número de 1 até 100:'))
    if n1 <= 100:
        break

resultado=alunos(n1)
print(resultado)


    
        