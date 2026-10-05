from tarefa import Tarefa
from lista_encadeada import ListaTarefas


lista = ListaTarefas()

tarefa1 = Tarefa(
    "Entregar relatório",
    "2026-10-09"
)

tarefa2 = Tarefa(
    "Fazer apresentação",
    "2026-10-06"
)

tarefa3 = Tarefa(
    "Estudar Python",
    "2026-10-12"
)

lista.inserir(tarefa1)
lista.inserir(tarefa2)
lista.inserir(tarefa3)

print("TAREFAS:")
lista.mostrar()
