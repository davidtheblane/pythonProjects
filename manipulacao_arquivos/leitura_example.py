try:
    with open('lista_compras.txt', 'r') as arquivo:
        print('lendo arquivo linha por linha')

        for linha in arquivo:
            # .strip() é MUITO importante. Ele remove espaços em branco
            # e quebras de linha invisíveis (o '\n') do início e fim da linha.
            print(f"Item: {linha.strip()}")

    # Podemos ler o arquivo todo de uma vez também:
    with open("lista_compras.txt", "r") as arquivo:
        conteudo_completo = arquivo.read()
        print("\nConteúdo completo de uma vez:")
        print(conteudo_completo)

except FileNotFoundError:
    print("\nERRO: O arquivo 'lista_compras.txt' não foi encontrado.")
    print("Certifique-se de que ele está na mesma pasta do seu script.")
