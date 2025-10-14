contatos = []

contato1 = {
    "nome": "Davi",
    "telefone": "1111-2222"
}

contatos.append(contato1)

contato2 = {
    "nome": "Dayane",
    "telefone": "3333-4444"
}

contatos.append(contato2)

for contato in contatos:
    print('--------------------')
    for chave, valor in contato.items():
        print(f"{chave.capitalize()}: {valor}")

print('--------------------')
