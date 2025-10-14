import random
import math  # Importamos o módulo no início do nosso script

# Agora podemos usar suas funções, sempre com o prefixo "math."
raiz_quadrada = math.sqrt(81)  # sqrt = square root
print(f"A raiz quadrada de 81 é: {raiz_quadrada}")

valor_pi = math.pi  # math.pi é uma variável dentro do módulo
print(f"O valor de PI é: {valor_pi}")


# Gera um número inteiro aleatório entre 1 e 100 (ambos inclusos)
numero_sorteado = random.randint(1, 100)
print(f"O número sorteado foi: {numero_sorteado}")

# Escolhe um item aleatório de uma lista
nomes = ["Ana", "Beto", "Carlos", "Gabi"]
ganhador = random.choice(nomes)
print(f"O ganhador do sorteio foi: {ganhador}")
