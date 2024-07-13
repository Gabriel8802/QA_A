print('Bem vindo a calculadora')
numero1 = float(input("qual é o primeiro numero?"))
operacao = input("digite a operação (+,-,*,/): ")
numero2 = float(input('qual é o segundo numero?'))

match operacao:
    case '+':
        print(numero1+numero2)

    case '-':
        print(numero1-numero2)

    case '*':
        print(numero1*numero2)

    case '/':
         print(numero1/numero2)
