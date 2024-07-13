secreto=12
acertou = False

while not acertou:
    palpite=int(input("digite um numero entre 1 e 100:"))

    if palpite == secreto:
        print("Parabéns! acertou o numero secreto")
        acertou = True
    elif palpite < secreto:
        print("O número é maior. Tente novamente!")
    else:
        print("O número é menor. Tente novamente!")

print("Fim de jogo")