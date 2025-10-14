secret_number = 11
stop_game = False

user_guess = int(
    input('Sabe qual o número secreto? Digite aqui seu palpite: '))

while stop_game == False:

    if (user_guess < secret_number):
        print('Muito baixo! Tente um número maior.')
        user_guess = int(input(''))

    elif (user_guess > secret_number):
        print('Muito alto! Tente um número menor.')
        user_guess = int(input(''))

    else:
        print('Parabéns voce acertou.')
        stop_game = True


# refatorado / corrigido
# secret_number = 11

# while True:

#     user_guess = int(
#         input('Sabe qual o número secreto? Digite aqui seu palpite: '))

#     if user_guess < secret_number:
#         print('Muito baixo! Tente um número maior.')
#     elif user_guess > secret_number:
#         print('Muito alto! Tente um número menor.')
#     else:
#         print('Parabéns, você acertou!')
#         break
