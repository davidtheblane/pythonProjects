print('=================')
print('Iterando uma lista')
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print(num * num)

print('=================')

print('Iterando um dicionário')
contato = {"nome": "Maria", "telefone": "9999-8888"}

for chave, valor in contato.items():
    print(f"Chave: {chave}, Valor: {valor}")
