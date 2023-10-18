# Escreva um programa em Python que solicite ao usuário que insira um ano (um número inteiro) e determine se o ano é bissexto ou não. O programa deve continuar pedindo ao usuário para inserir anos até que ele decida parar.

# Um ano bissexto é um ano que é divisível por 4, com exceção dos anos que são divisíveis por 100. No entanto, anos divisíveis por 400 também são considerados bissextos. Em outras palavras:

# **Anos divisíveis por 4 são bissextos (por exemplo, 2004, 2008, 2012).**

# **Anos divisíveis por 100 não são bissextos**

# Instruções:

# Solicite ao usuário que insira um ano.

# Verifique se o ano é bissexto de acordo com as regras mencionadas anteriormente.

# Se o ano for bissexto, imprima "O ano [ano] é bissexto.".

# Se o ano não for bissexto, imprima "O ano [ano] não é bissexto.".

# Pergunte ao usuário se ele deseja verificar outro ano.

# Se o usuário quiser verificar outro ano, repita o processo. Caso contrário, encerre o programa.

def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    return False

while True:
    ano = int(input("Digite um ano (0 para sair): "))
    
    if ano == 0:
        break
    
    if verificar_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
