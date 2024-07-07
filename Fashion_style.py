cupom10=float(input("digite o valor da compra:"))
if cupom10 >= 250 and cupom10 <= 500:
    print('PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00')
elif cupom10 > 500:
    print('PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%')
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")
