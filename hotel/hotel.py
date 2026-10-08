from pessoas import Recepcionista, TecnicoManutencao


class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = []
        self.hospedes = []
        self.funcionarios = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def adicionar_hospede(self, hospede):
        self.hospedes.append(hospede)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def find_quarto(self, numero):
        for q in self.quartos:
            if q.numero == numero:
                return q
        return None

    def find_recepcionista(self):
        for f in self.funcionarios:
            if isinstance(f, Recepcionista):
                return f
        return None

    def find_tecnico(self):
        for f in self.funcionarios:
            if isinstance(f, TecnicoManutencao):
                return f
        return None

    def find_hospede(self, nome):
        for h in self.hospedes:
            if h.nome.lower() == nome.lower():
                return h
        return None