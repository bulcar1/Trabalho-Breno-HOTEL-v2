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
        for quarto in self.quartos:
            if quarto.numero == numero:
                return quarto
        return None

    def find_recepcionista(self):
        for funcionario in self.funcionarios:
            if isinstance(funcionario, Recepcionista):
                return funcionario
        return None

    def find_tecnico(self):
        for funcionario in self.funcionarios:
            if isinstance(funcionario, TecnicoManutencao):
                return funcionario
        return None

    def find_hospede(self, nome):
        for hospede in self.hospedes:
            if hospede.nome.lower() == nome.lower():
                return hospede
        return None