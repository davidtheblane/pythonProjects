# FORMA ANTIGA
numeros = [1, 2, 3, 4, 5]
quadrados = []  # 1. Cria lista vazia

for n in numeros:  # 2. Faz um loop
    quadrados.append(n * n)  # 3. Adiciona o resultado

print(quadrados)
# Saída: [1, 4, 9, 16, 25]

####################################################

# FORMA NOVA
numeros = [1, 2, 3, 4, 5]

quadrados = [n * n for n in numeros]  # Faz tudo em uma linha!

print(quadrados)
# Saída: [1, 4, 9, 16, 25]

####################################################

# FORMA NOVA COM IF
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Pegar apenas os números pares e multiplicá-los por 2
resultado = [n * 2 for n in numeros if n % 2 == 0]

print(resultado)
# Saída: [4, 8, 12, 16]
