# Pedindo o nome do usuário (string)
nome_usuario = input("Qual é o seu nome? ")

# Pedindo o ano de nascimento (precisamos converter para int)
ano_nascimento_str = input("Em que ano você nasceu? ")
ano_nascimento = int(ano_nascimento_str) # Converte a string para inteiro

# Fazendo um cálculo simples
ano_atual = 2024
idade_aproximada = ano_atual - ano_nascimento

# Exibindo os resultados
print(f"Olá, {nome_usuario}!")
print(f"Você tem aproximadamente {idade_aproximada} anos.")

# Usando um operador de comparação
e_maior_de_idade = idade_aproximada >= 18
print(f"É maior de idade? {e_maior_de_idade}")