from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def mostrar_informacoes(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_informacoes(self):
        return f"Funcionário: {self.nome} , Idade: {self.idade} , Salário: {self.salario:.2f}€"


class Gerente(Funcionario):
    def mostrar_informacoes(self):
        return f"Gerente: {self.nome} , Idade: {self.idade} , Salário: {self.salario:.2f}€"

    def gerar_relatorio(self, funcionarios):
        for f in funcionarios:
            print(f.mostrar_informacoes())


class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self.id_func = id_func
        self.turno = turno

    def mostrar_informacoes(self):
        return f"Recepcionista: {self.nome} (ID: {self.id_func}) , Turno: {self.turno}"

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)
        return f"Hóspede {hospede.nome} registado com sucesso."

    def listar_hospedes(self, lista_hospedes):
        if not lista_hospedes:
            print("Nenhum hóspede registado.")
            return
        for h in lista_hospedes:
            print(h.mostrar_informacoes())


class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario,):
        super().__init__(nome, idade, salario)

    def mostrar_informacoes(self):
        return f"Técnico: {self.nome}"

    def registrar_reparo(self, descricao):
        return f"Reparo registado: {descricao}"


class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    def __init__(self, nome, id_func, idade, salario, turno):
        Funcionario.__init__(self, nome, idade, salario)
        self.id_func = id_func
        self.turno = turno
       


    def registrar_hospede(self, nome_hospede):
        return f"Hóspede {nome_hospede} registado pela receção técnica."
    

    def registrar_reparo(self, descricao):
        return f"Reparo registado pela receção técnica: {descricao}"

    def mostrar_informacoes(self):
        return f"Técnico de Receção: {self.nome} (ID: {self.id_func})"


class Hospede(Pessoa):
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self.dias_estadia = dias_estadia
        self.quarto = None
        if quarto:
            self.atribuir_quarto(quarto)

    def atribuir_quarto(self, quarto):
        # Interligação direta com a classe Quarto
        if quarto.ocupado:
            raise ValueError("Este quarto já está ocupado.")
        if self.quarto:
            self.quarto.desocupar()
        self.quarto = quarto
        quarto.ocupar()

    def calcular_conta(self):
        if not self.quarto:
            return 0
        return self.dias_estadia * self.quarto.preco_diaria

    def mostrar_informacoes(self):
        num_quarto = self.quarto.numero if self.quarto else "Sem quarto"
        return f"Hóspede: {self.nome} , Idade: {self.idade} , Dias: {self.dias_estadia} , Quarto: {num_quarto}"

    def checkout(self):
        if self.quarto:
            num = self.quarto.numero
            self.quarto.desocupar()
            self.quarto = None
            return f"{self.nome} realizou checkout do quarto {num}."
        return f"{self.nome} não está hospedado num quarto."