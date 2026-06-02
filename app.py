import utils as u
import cliente as c
import profissionais as p
import catalogo as ct
import p_venda as v
import estoque as e


def main():
    items = ["Clientes", "Profissionais", "Catálogo", "Produtos para Venda", "Estoque", "Sair"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("Digite a opção desejada: ", 1, 6)
        if op == 1:
            c.main()
        elif op == 2:
            p.main()
        elif op == 3:
            ct.main()
        elif op == 4:
            v.main()
        elif op == 5:
            e.main()
        else:
            break

main() 


