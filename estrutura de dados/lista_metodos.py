# 1 .append(item): Adiciona um item ao final da lista.
# 2 .insert(indice, item): Adiciona um item em uma posição específica.
# 3 .pop(indice): Remove e retorna o item de uma posição específica. Se você não especificar o índice, ele remove o último item.
# 4 .remove(item): Remove a primeira ocorrência de um item com um valor específico.
# 5 Função len(lista): Embora não seja um método (não se usa o .), a função len() é essencial. Ela retorna o tamanho (quantidade de itens) da lista.

convidados = ["Ana", "Beto"]

convidados.append("Carlos")
convidados.insert(0, "Gabi")
convidados.remove("Beto")

print(convidados)
print(f"Total de convidados: {len(convidados)}")
