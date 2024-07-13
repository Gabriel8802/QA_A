#if- condição se valor for atendido
idade=int(input("qual a sua idade?"))
if idade > 18 and idade < 60:
    print("você é maior de idade")
#elif- um meio termo, ou uma subcondição
elif idade >=60:
    print("você é experiente")
#else=alternativa se não condizer com o valor pré-estabelecido no programa
else:
    print("você é menor de idade")