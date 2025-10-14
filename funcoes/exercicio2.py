def verificar_maioridade(idade):
    if (idade >= 18):
        return True
    else:
        return False


pode_entrar = verificar_maioridade(15)

if pode_entrar:
    print('Acesso permitido')
else:
    print('Acesso negado')
