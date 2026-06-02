import utils as u

#CATALOGO
catalogo = {}
n_procedimento = []
v_procedimento = []
def cadastro_procedimento ():
    print(f"\n{"-" * 10} Cadastro de procedimentos {"-" * 10}")
    while True:
            nome = input(f"Nome do procedimento ('n' para sair):")
            if nome == 'n':
                break
            else:
                valor = int(input(f"Preço do procedimento: "))
                v_procedimento.append(valor)
                n_procedimento.append(nome)

                catalogo[nome] = valor
    return


def main():
    items = ["Cadastrar Procedimentos", "Listar Procedimentos", "Sair"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("Digite a opção desejada: ", 1, 3)
        if op == 1:
            cadastro_procedimento()
        elif op == 2:
            print(f"\n {catalogo}")
            pass
        else:
            break
