ARQUIVO_TAREFAS = 'tarefas.txt'


def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, 'r') as arquivo:
            tarefas = [linha.strip() for linha in arquivo]
        return tarefas
    except FileNotFoundError:
        return []


def salvar_tarefas(listar_tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as arquivo:
        for tarefa in listar_tarefas:
            arquivo.write(f"{tarefa}\n")


def listar_tarefas(lista_de_tarefas):
    print("\n--- Suas Tarefas ---")
    if not lista_de_tarefas:  # Uma forma "Pythônica" de checar se a lista está vazia
        print("Nenhuma tarefa na lista.")
    else:
        # enumerate é uma função útil que nos dá o índice e o valor
        for i, tarefa in enumerate(lista_de_tarefas):
            print(f"{i + 1}. {tarefa}")
    print("--------------------")


def adicionar_tarefa(lista_de_tarefas):
    nova_tarefa = input("Digite a nova tarefa: ")
    lista_de_tarefas.append(nova_tarefa)
    salvar_tarefas(lista_de_tarefas)
    print("Tarefa adicionada com sucesso!")


def remover_tarefa(lista_de_tarefas):

    if not lista_de_tarefas:
        print("--------------------")
        print("Nenhuma tarefa na lista.")
        return

    listar_tarefas(lista_de_tarefas)

    try:
        numero_tarefa = int(
            input("Digite o número da tarefa que deseja remover."))

        if 1 <= numero_tarefa <= len(lista_de_tarefas):
            lista_de_tarefas.pop(numero_tarefa - 1)
            salvar_tarefas(lista_de_tarefas)
            print("Tarefa removida com sucesso!")
        else:
            print("--------------------")
            print("Número inválido. Por favor, digite um número da lista.")
            print("--------------------")

    except ValueError:
        print('Valor não suportado, precisa ser um número válido')
        return


# --- Loop Principal do Programa ---
tarefas = carregar_tarefas()

while True:
    print("\nMenu do App de Tarefas:")
    print("1. Listar tarefas")
    print("2. Adicionar nova tarefa")
    print("3. Remover tarefa")
    print("4. Sair")
    print("--------------------")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        listar_tarefas(tarefas)
    elif escolha == '2':
        adicionar_tarefa(tarefas)
    elif escolha == '3':
        remover_tarefa(tarefas)
    elif escolha == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
