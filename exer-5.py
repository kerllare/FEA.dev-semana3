# Você está comprando uma sobremesa em uma cafeteria. O preço da sobremesa pode variar, e você tem um voucher 
# que cobre até $20. 
# Se a sobremesa custar mais, você precisará pagar a diferença. Se custar menos,
# você economizará o valor restante do voucher.

# Crie um programa em Python que solicite o preço da sobremesa que você deseja comprar. 
# Em seguida, o programa deve calcular se a operação foi vantajosa e quanto você economizou
# ou precisa pagar a mais.

# Se o preço da sobremesa for maior que 20, o programa deve imprimir "Você precisa pagar X a mais."
# (onde X é a diferença entre o preço da sobremesa e 20).

# Se o preço da sobremesa for igual a 20, o programa deve imprimir "Você não precisa pagar nada a mais."

# Se o preço da sobremesa for menor que 20, o programa deve imprimir "Você economizou X." 
# (onde X é a diferença entre 20 e o preço da sobremesa).

# Solicite o preço da sobremesa
# Defina o preço máximo coberto pelo voucher
# Calcule a diferença entre o preço da sobremesa e o valor do voucher
# Verifi1que se você precisa pagar a mais, economizou ou não precisa pagar nada a mais

# Solicita o preço da sobremesa
preco_sobremesa = float(input("Digite o preço da sobremesa que deseja comprar: $"))

# Define o preço máximo coberto pelo voucher
preco_maximo_voucher = 20.0

# Calcula a diferença entre o preço da sobremesa e o valor do voucher
diferenca = preco_sobremesa - preco_maximo_voucher

# Verifica se você precisa pagar a mais, economizou ou não precisa pagar nada a mais
if diferenca > 0:
    print(f"Você precisa pagar ${diferenca:.2f} a mais.")
elif diferenca == 0:
    print("Você não precisa pagar nada a mais.")
else:
    economia = abs(diferenca)
    print(f"Você economizou ${economia:.2f}.")


