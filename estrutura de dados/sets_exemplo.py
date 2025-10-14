# Não permite itens duplicados.
# É desordenado, ou seja, não há garantia da ordem dos itens.
# Sintaxe: Usa chaves {}, mas sem os pares chave: valor.
# Quando usar? O uso mais comum de um set é para remover rapidamente itens duplicados de uma lista.

numeros_com_duplicatas = [1, 2, 2, 3, 4, 3, 5, 5, 5]
print(f"Lista original: {numeros_com_duplicatas}")

# Convertendo a lista para um set para remover as duplicatas
numeros_unicos = set(numeros_com_duplicatas)
print(f"Set com números únicos: {numeros_unicos}")
