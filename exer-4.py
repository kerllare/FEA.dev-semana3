# Você descobriu um sebo perto da sua casa e resolve dar uma olhada e encontra muitos títulos interessantes. Mas como você não está nadando em dinheiro, terá que fazer algumas escolhas. 
# - Escreva um programa que retorne se você deverá comprar ou não o livro, considerando que:
# - Ele precisa estar na sua wishlist (nada de comprar por impulso);
# - O preço do sebo deve ser mais barato do que na inter


# a) Você deverá comprar Moby Dick?

# b) Você deverá comprar Crime e Castigo?

# c) Você deverá comprar a Odisseia?


wishlist = ['Moby Dick', 'Helena', 'A Origem das Espécies', 'Grande Sertão: Veredas', 'Odisseia', 'Rápido e Devagar', 'Sidarta']

precos_sebo = {'Odisseia': 50, 'Jane Eyre': 61, 'A Divina Comédia': 56, 'Helena': 10, 'Moby Dick': 55, 'Crime e Castigo': 20}
precos_internet = {'Odisseia': 30, 'Jane Eyre': 32, 'A Divina Comédia': 22, 'Helena': 26, 'Moby Dick': 145, 'Crime e Castigo': 80}

def deve_comprar_livro(livro):
    if livro in wishlist:
        preco_sebo = precos_sebo.get(livro, None)
        preco_internet = precos_internet.get(livro, None)
        if preco_sebo is not None and preco_internet is not None and preco_sebo < preco_internet:
            return f"Você deve comprar {livro}"
    return f"Você não deve comprar {livro}"

# Verificando se deve comprar cada livro
a = deve_comprar_livro('Moby Dick')
b = deve_comprar_livro('Crime e Castigo')
c = deve_comprar_livro('Odisseia')

print(a)
print(b)
print(c)
