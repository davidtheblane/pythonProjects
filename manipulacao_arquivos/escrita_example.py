# Modo "w": Apaga o conteúdo anterior e escreve
try:
    with open("convidados.txt", "w") as arquivo:
        arquivo.write("Ana\n")  # Precisamos adicionar o \n manualmente
        arquivo.write("Beto\n")
    print("Arquivo 'convidados.txt' criado/sobrescrito.")

    # Modo "a": Adiciona ao final
    with open("convidados.txt", "a") as arquivo:
        arquivo.write("Carlos\n")
        arquivo.write("Gabi\n")
    print("Novos nomes adicionados ao final do arquivo.")

    # Agora, vamos ler o arquivo para ver o resultado final
    print("\n--- Conteúdo final do 'convidados.txt' ---")
    with open("convidados.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(f"Ocorreu um erro: {e}")
