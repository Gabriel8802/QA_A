def calcular_preco_total(valor_total,desconto_percentual):
    desconto = valor_total*(desconto_percentual / 100)
    preco_com_desconto = valor_total - desconto
    return preco_com_desconto

valor_da_compra=float(input('Digite o valor da compra:'))
desconto_oferecido=int(input('Digite a porcentagem de desconto:'))

preco_final = calcular_preco_total(valor_da_compra,desconto_oferecido)
print('Preço total de desconto é: R$',preco_final)