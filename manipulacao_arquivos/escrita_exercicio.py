newTask = input('Digite uma nova tarefa: ')

try:
    with open('tarefas.txt', 'a') as arquivo:
        arquivo.write(f"{newTask}\n")
        print('Tarefa Adicionada')


except FileExistsError:
    print("\nERRO: O arquivo 'lista_compras.txt' não foi gravado.")
