# Desafio: fazer uma pirâmide do Mário usando '#' e com o input do usuário

# Solicita ao usuário o tamanho da pirâmide e converte a entrada para um número inteiro.
x = int(input('Tamanho da pirâmide: '))

# Loop que itera de 1 até x, inclusive.
for i in range(1, x + 1):
    # Diminui o valor de x em 1 a cada iteração para ajustar os espaços em branco à esquerda.
    x -= 1
    
    # Imprime uma sequência de espaços em branco para criar o recuo.
    # O número de espaços é determinado pelo valor atual de x.
    # O argumento end="" garante que a próxima impressão seja na mesma linha.
    print(" " * x, end="")
    
    # Imprime uma sequência de "#" para construir a linha da pirâmide.
    # O número de "#" é determinado pelo valor de i.
    print('#' * i)
