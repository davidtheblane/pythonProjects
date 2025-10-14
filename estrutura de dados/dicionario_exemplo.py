# Criando um dicionário para representar um aluno
aluno = {
    "nome": "Davi",
    "idade": 38,
    "curso": "Engenharia",
    "materias_cursadas": ["Cálculo", "Física"]
}

# Acessando valores pela chave
print(f"Nome do aluno: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")

# O valor pode ser uma lista, que podemos acessar normalmente
print(f"Primeira matéria cursada: {aluno['materias_cursadas'][0]}")

# Modificando um valor existente
print("\nAluno trocou de curso...")
aluno['curso'] = "Ciência da Computação"
print(f"Novo curso: {aluno['curso']}")

# Adicionando um novo par chave-valor
print("\nAdicionando cidade...")
aluno['cidade'] = "Santos"

# Exibindo o dicionário completo
print(f"\nDados completos do aluno: {aluno}")
