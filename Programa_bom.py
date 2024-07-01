
despesas = []
valores = []
saldo = float(input('Qual é o seu saldo?'))

while True:
    despesa = input('Nomeie uma despesa (ou digite "no" para finalizar): ')
    if despesa.lower() == 'no':
       print=(despesas,valores)

    valor_input = input('Digite o valor da despesa (ou digite "no" para finalizar): ')
    if valor_input.lower() == 'no':
        print=(despesas,valores)

    valor = float(valor_input)
    despesas.append(despesa)
    valores.append(valor)



    