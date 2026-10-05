class Tarefa:
    def __init__(self, titulo, prazo):
        self.titulo = titulo
        self.prazo = prazo
        self.proximo = None

    def __str__(self):
        return f"{self.titulo} | Prazo: {self.prazo}"
