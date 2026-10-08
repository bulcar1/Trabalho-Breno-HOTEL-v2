from hotel import Hotel
from quartos import QuartoSimples, QuartoLuxo
from pessoas import (
    Hospede,
    Gerente,
    Recepcionista,
    TecnicoManutencao,
    TecnicoRecepcao
)


def ler_num(texto, tipo=int):
    while True:
        try:
            return tipo(input(texto).replace(",", "."))
        except ValueError:
            print("Número inválido.")


def menu():
    print("Hotel")
    print("1- Registar hóspede")
    print("2- Registar funcionário")
    print("3- Reservar quarto")
    print("4- Listar quartos")
    print("5- Listar hóspedes")
    print("6- Listar funcionários")
    print("7- Fazer checkout")
    print("8- Técnico de Manutenção/Reparação")
    print("9- Adicionar quarto")
    print("0- Sair")

def registar_hospede(hotel):
    recep = hotel.find_recepcionista()
    if not recep:
        print("Erro: Registe primeiro um recepcionista.")
        return
    nome = input("Nome: ")
    idade = ler_num("Idade: ")
    dias = ler_num("Dias de estadia: ")
    try:
        hospede = Hospede(nome, idade, dias)
        print(recep.registrar_hospede(hospede, hotel.hospedes))
    except ValueError as e:
        print(f"Erro: {e}")


def registar_funcionario(hotel):
    print("1- Gerente, 2- Recepcionista , 3- Técnico Manutençao , 4- Técnico Receção")
    tipo = ler_num("Tipo: ")
    nome = input("Nome: ")
    idade = ler_num("Idade: ")
    salario = ler_num("Salário: ", float)

    try:
        if tipo == 1:
            f = Gerente(nome, idade, salario)
        elif tipo == 2:
            id_f = ler_num("ID: ")
            turno = input("Turno: ")
            f = Recepcionista(nome, id_f, idade, salario, turno)

            f = TecnicoManutencao(nome, idade, salario)
        elif tipo == 3:
            id_f = ler_num("ID: ")
            turno = input("Turno: ")
            
  
            f = TecnicoRecepcao(nome, id_f, idade, salario, turno)
        else:
            print("Tipo inválido.")
            return
        hotel.adicionar_funcionario(f)
        print(f"{nome} registado com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")


def reservar_quarto(hotel):
    hospede = hotel.find_hospede(input("Nome do hóspede: "))
    if not hospede:
        print("Hóspede não encontrado.")
        return
    quarto = hotel.find_quarto(ler_num("Número do quarto: "))
    if not quarto:
        print("Quarto não encontrado.")
        return
    try:
        hospede.atribuir_quarto(quarto)
        print(f"Quarto {quarto.numero} reservado! Total: {hospede.calcular_conta():.2f}€")
    except ValueError as e:
        print(f"Erro: {e}")


def fazer_checkout(hotel):
    hospede = hotel.find_hospede(input("Nome do hóspede: "))
    if not hospede:
        print("Hóspede não encontrado.")
        return
    conta = hospede.calcular_conta()
    print(hospede.checkout())
    print(f"Total a pagar: {conta:.2f}€")


def registar_reparo(hotel):
    tecnico = hotel.find_tecnico()
    if not tecnico:
        print("Erro: Registe primeiro um técnico de manutenção.")
        return
    print(tecnico.registrar_reparo(input("Descrição do reparo: ")))


def novo_quarto(hotel):
    tipo = ler_num("1- Simples , 2- Luxo: ")
    num = ler_num("Número: ")
    preco = ler_num("Preço/diária: ", float)

    if hotel.find_quarto(num):
        print("Já existe um quarto com esse número.")
        return
    try:
        q = QuartoSimples(num, preco) if tipo == 1 else QuartoLuxo(num, preco)
        hotel.adicionar_quarto(q)
        print(f"Quarto {num} criado com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")


def main():
    hotel = Hotel("Hotel Central")

    while True:
        menu()
        opcao = input("Opção: ").strip()

        if opcao == "1":
            registar_hospede(hotel)
        elif opcao == "2":
            registar_funcionario(hotel)
        elif opcao == "3":
            reservar_quarto(hotel)
        elif opcao == "4":
            for q in hotel.quartos:
                print(q.mostrar_informacoes())
        elif opcao == "5":
            recep = hotel.find_recepcionista()
            if recep:
                recep.listar_hospedes(hotel.hospedes)
            else:
                print("Registe primeiro um recepcionista.")
        elif opcao == "6":
            for f in hotel.funcionarios:
                print(f.mostrar_informacoes())
        elif opcao == "7":
            fazer_checkout(hotel)
        elif opcao == "8":
            registar_reparo(hotel)
        elif opcao == "9":
            novo_quarto(hotel)
        elif opcao == "0":
            print("A sair...")
            break


if __name__ == "__main__":
    main()