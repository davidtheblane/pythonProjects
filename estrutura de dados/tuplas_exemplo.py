# Sintaxe: Usa parênteses () em vez de colchetes [].
# Quando usar? Quando você tem uma coleção de dados que não deve mudar nunca, como coordenadas (x, y), meses do ano ou configurações fixas.

# Criando uma tupla
coordenadas = (40.71, -74.00)  # Latitude e Longitude de NY
print(f"Coordenadas: {coordenadas}")

# Acessar é igual à lista
print(f"Latitude: {coordenadas[0]}")

# Se você tentar modificar, dará erro. A linha abaixo está comentada porque quebraria o programa:
# coordenadas[0] = 50 # TypeError: 'tuple' object does not support item assignment
