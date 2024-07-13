vogais = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
palavra = input("Digite uma palavra: ")

contador = 0

for letra in palavra:
    if letra.lower() in vogais:  # Convertendo a letra para minúscula para considerar tanto maiúsculas quanto minúsculas
        contador += 1

print(f"A palavra é '{palavra}' e tem {contador} vogais.")