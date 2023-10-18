# Escreva um código que conte quantas vezes a letra "a" aparece em duas estrofes do famoso hit de Lady Gaga:

ad_romance = """Rah, rah-ah-ah-ah
                 Roma, roma-ma
                 Gaga, ooh-la-la
                 Want your bad romance

                 Rah, rah-ah-ah-ah
                 Roma, roma-ma
                 Gaga, ooh-la-la
                 Want your bad romance"""

# Transforma o texto em minúsculas para garantir que todas as letras "a" sejam contadas
ad_romance = ad_romance.lower()

# Conta quantas vezes a letra "a" aparece
quantidade_de_a = ad_romance.count('a')

print(f"A letra 'a' aparece {quantidade_de_a} vezes nas estrofes de 'Bad Romance'.")
