#Esreva um código que receba o input de um número e verifique se ele é primo ou não. 
# Solicita ao usuário que insira um número
# Verifica se o número é maior que 1
# Inicializa uma variável para contar os divisores
# Loop para verificar se o número é primo
# Se encontrarmos um divisor, podemos parar de verificar
# Se não houver divisores além de 1 e o próprio número, é primo

# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Inicializa uma variável para contar os divisores
    divisores = 0
    
    # Loop para verificar se o número é primo
    for i in range(2, numero):
        if numero % i == 0:
            divisores += 1
            break  # Se encontrarmos um divisor, podemos parar de verificar
    
    # Se não houver divisores além de 1 e o próprio número, é primo
    if divisores == 0:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print(f"{numero} não é um número primo, pois é menor ou igual a 1.")
