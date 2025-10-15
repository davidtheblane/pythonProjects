try:
    with open('objetivos.txt', 'r') as arquivo:

        primeira_linha = arquivo.readline()
        # .strip() remove o \n e evita a linha extra
        print(primeira_linha.strip())

except FileNotFoundError:
    print("\nERRO: O arquivo 'objetivos.txt' não foi encontrado.")
    print("Certifique-se de que ele está na mesma pasta do seu script.")
