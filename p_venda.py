import utils as u

#PRODUTOS PARA VENDA
produtos = {}
n_produto = []
p_produto = []
def cadastro_produtos_vendas ():
    print(f"{"-" * 10} Cadastro de Produtos para Vendas {"-" * 10}")
    while True:
            nome = input(f"Nome do produto ('n' para sair):")
            if nome == 'n':
                break
            else:
                preco = int(input(f"Preço do produto: "))
                p_produto.append(preco)
                n_produto.append(nome)

                produtos[nome] = preco
    return

# produtos_vendas()
# print(f"\n {n_produto}")
# print(f"\n {p_produto}")
# print(f"\n {produtos}")

def main():
    items = ["Cadastro de Produtos para Vendas", "Listar Produtos para Vendas", "Sair"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("Digite a opção desejada: ", 1, 3)
        if op == 1:
            cadastro_produtos_vendas()
        elif op == 2:
            print(f"\n {produtos}")
            pass
        else:
            break