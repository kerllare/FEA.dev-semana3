# Desafio: fazer uma pirâmide do Mário usando '#' e com o input do usuário

x = int(input('Tamanho pirâmide: '))
for i in range(1, x +1):
    x -= 1
    print(" " * x, end="")
    print('#' * i)