from abc import ABC, abstractmethod

class Quarto(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self._preco_diaria = 0
        self.preco_diaria = preco_diaria
        self.ocupado = False

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, valor):
        if valor < 0:
            raise ValueError("Preço inválido.")
        self._preco_diaria = valor

    def ocupar(self):
        self.ocupado = True

    def desocupar(self):
        self.ocupado = False

    @abstractmethod
    def mostrar_informacoes(self):
        pass


class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Simples", preco_diaria)

    def mostrar_informacoes(self):
        status = "Ocupado" if self.ocupado else "Livre"
        return f"Quarto {self.numero}, ({self.tipo}),{self.preco_diaria:.2f} , {status}"


class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Luxo", preco_diaria)

    def mostrar_informacoes(self):
        status = "Ocupado" if self.ocupado else "Livre"
        return f"Quarto {self.numero} ({self.tipo}) | {self.preco_diaria:.2f}€ | {status}"