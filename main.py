tarefas = []

while True:
    tarefas.sort()
    nova_tarefa = input('Informe suas tarefas do dia ou deixe vazio para encerrar e exibir a lista: ')

    if nova_tarefa != '':
        tarefas.append(nova_tarefa)
        continue
    else:
        break
    
for tarefa in tarefas:
    print(tarefa)

