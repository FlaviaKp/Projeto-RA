import utils as u

#ESTOQUE
estoque = {}
no_produto = []
q_produto = []
def produtos_estoque ():
    print(f"\n {"-" * 10} Cadastro do Estoque {"-" * 10}")
    while True:
            nome = input(f"Nome do produto ('n' para sair): ")
            if nome == 'n':
                break
            else:
                quantidade = int(input(f"Quantidade disponivel do produto: "))
                q_produto.append(quantidade)
                no_produto.append(nome)

                estoque[nome] = quantidade
    return


def main():
    items = ["Cadastro do Estoque", "Listar Estoque", "Listar produtos utilizados em cada procedimento", "Sair"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("Digite a opção desejada: ", 1, 4)
        if op == 1:
            produtos_estoque()
        elif op == 2:
            print(f"\n {estoque}")
        elif op == 3:
            # TODO: Relacionar produtos utilizados com os procedimentos
            pass
        else:
            break