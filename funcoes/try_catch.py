try:
    multiplicador = int(input('Escolha um número para gerar a tabuada: '))

    for num in range(1, multiplicador):
        if (num == 1):
            print(f"{multiplicador} X {num} = {multiplicador * num}")
        else:
            print(f"{multiplicador} X {num+1} = {multiplicador * (num+1)}")

except ValueError:
    print('Entrada inválida. Por favor digite um número.')

# outra maneira mais simples
# for num in range(1, 11):
#     print(f"{multiplicador} X {num} = {multiplicador * num}")
