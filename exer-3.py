# Consultar idade para votar

idade = float(input("Digite sua idade: "))

if idade < 16:
    print('Não pode votar')
    
elif idade > 15 and idade < 18 or idade > 70:
    print('Direito a voto, mas não obrigatório')
    
elif idade in range(18, 70):
 print('Voto obrigatório')