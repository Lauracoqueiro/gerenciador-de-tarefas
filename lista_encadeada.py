from tarefa import Tarefa


class ListaTarefas:

    def __init__(self):
        self.inicio = None

    def inserir(self, nova_tarefa):

        # Lista vazia
        if self.inicio is None:
            self.inicio = nova_tarefa
            return

        # Inserir antes do primeiro
        if nova_tarefa.prazo < self.inicio.prazo:
            nova_tarefa.proximo = self.inicio
            self.inicio = nova_tarefa
            return

        # Procurar posição correta
        atual = self.inicio

        while (
            atual.proximo is not None
            and atual.proximo.prazo <= nova_tarefa.prazo
        ):
            atual = atual.proximo

        nova_tarefa.proximo = atual.proximo
        atual.proximo = nova_tarefa

    def mostrar(self):

        if self.inicio is None:
            print("Nenhuma tarefa cadastrada.")
            return

        atual = self.inicio
        contador = 1

        while atual is not None:
            print(
                f"{contador}. "
                f"{atual.titulo} | Prazo: {atual.prazo}"
            )

            atual = atual.proximo
            contador += 1

    def remover(self, titulo):

        if self.inicio is None:
            return False

        # Remover a primeira tarefa
        if self.inicio.titulo.lower() == titulo.lower():
            self.inicio = self.inicio.proximo
            return True

        atual = self.inicio

        while atual.proximo is not None:

            if atual.proximo.titulo.lower() == titulo.lower():

                atual.proximo = atual.proximo.proximo

                return True

            atual = atual.proximo

        return False
