# Crie um programa que peça para digitar um número constantemente sem limite, até que o usário digite o número 0. 
# Em seguida mostre a soma de todos os valores inputados, 
# e a quantidade de números que foram inputados

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        break
    
    soma += numero
    quantidade += 1

print(f"A soma dos números inseridos é: {soma}")
print(f"Foram inseridos {quantidade} números.")
