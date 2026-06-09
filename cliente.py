import utils as u
import repository.appDbContext as r

#CLIENTES
clientes = {}

def cadastro_clientes():

    print(f"\n {"-" * 10} Cadastro de Cliente {"-" * 10}")

    cpf = int(input("Informe o CPF do cliente: "))
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    problemas_saude= input("Possui problemas de saúde? (diabetes, alergias, etc. ou 'Não'):" )
    
    if idade < 18:
        print(f"\n {"*" * 10}Necessário ter 18 anos.\n {"*" * 10}")
        return False
    

    clientes[cpf] = {
        "cpf": cpf,
        "nome": nome,
        "idade": idade,
        "problemas_saude": problemas_saude
    }
    cadastra_db = r.cadastra_db(cpf, nome, idade, problemas_saude)

    print(cadastra_db)
    return True

def editar_clientes():
    print(f"\n {"-" * 10} Editar cliente {"-" * 10}")

    cpf = int(input("Informe o CPF do cliente: "))
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    problemas_saude= input("Possui problemas de saúde? (diabetes, alergias, etc. ou 'Não'):" )
    
    if idade < 18:
        print(f"\n {"*" * 10}Necessário ter 18 anos.\n {"*" * 10}")
        return False


    r.editar_clientes(cpf, nome, idade, problemas_saude)

    return

def excluir_cliente():
    print(f"\n {"-" * 10} Excluir cliente {"-" * 10}")

    cpf = int(input("Informe o CPF do cliente: "))
    
    r.excluir_cliente(cpf)

    return
# cadastro_clientes()
# print(clientes)

def main():
    items = ["Cadastrar Cliente", "Editar Cliente", "Excluir Cliente", "Listar Clientes", "Voltar ao menu anterior"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("\nDigite a opção desejada: ", 1, 5)
        if op == 1:
            cadastro_clientes()
        elif op == 2:
            editar_clientes()
        elif op == 3:
            excluir_cliente()
            pass
        elif op == 4:
            r.listar_clientes()  #Chamar módulo de listar clientes
        else:
            break
