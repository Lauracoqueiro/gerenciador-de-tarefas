from ia import extrair_tarefa
from tarefa import Tarefa
from lista_encadeada import ListaTarefas


lista = ListaTarefas()


def adicionar_tarefa():

    frase = input("\nDigite a tarefa: ")

    try:

        resultado = extrair_tarefa(frase)

        nova_tarefa = Tarefa(
            resultado["titulo"],
            resultado["prazo"]
        )

        lista.inserir(nova_tarefa)

        print("\nTarefa adicionada com sucesso!")
        print(f"Título: {nova_tarefa.titulo}")
        print(f"Prazo: {nova_tarefa.prazo}")

    except Exception as erro:

        print("\nErro ao adicionar tarefa:")
        print(erro)


def listar_tarefas():

    print("\n========== TAREFAS ==========")

    lista.mostrar()

    print("==============================")


def remover_tarefa():

    titulo = input("\nDigite o título da tarefa que deseja remover: ")

    removida = lista.remover(titulo)

    if removida:
        print("\nTarefa removida com sucesso!")
    else:
        print("\nTarefa não encontrada.")


def menu():

    while True:

        print("\n")
        print("===================================")
        print("       GERENCIADOR DE TAREFAS")
        print("===================================")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            adicionar_tarefa()

        elif opcao == "2":

            listar_tarefas()

        elif opcao == "3":

            remover_tarefa()

        elif opcao == "4":

            print("\nPrograma encerrado.")
            break

        else:

            print("\nOpção inválida.")


menu()
