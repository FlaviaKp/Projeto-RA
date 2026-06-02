import sqlite3
import utils as u

#CLIENTES
clientes = {}

def cadastro_clientes():
    connection = sqlite3.connect("meu_banco.db") #criar o banco de dados/se ja existir o db, ele so conecta -->> database
    carlos = connection.cursor() #Carlos é o robo executa as funções dentro do banco de dados --> grava, le // connection.cursor -> pega a função de cursor(robo) do sqlite3

    carlos.execute(""" 
    CREATE TABLE IF NOT EXISTS clientes(
                cpf INTEGER PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                problemas_saude TEXT NOT NULL
    )
    """) #cria a tabela cliente se nao existir no banco de dados

    
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

    carlos.execute(
        "INSERT INTO clientes(cpf, nome, idade, problemas_saude) VALUES (?,?,?,?)",
        (cpf, nome, idade, problemas_saude)
    ) #insere  os dados do cliente no banco de dados

    connection.commit() #salva as alterações no db.
    connection.close() #fecha a conecção no db.

    print("Cadastro bem sucedido!!")
    return True

# cadastro_clientes()
# print(clientes)

def main():
    items = ["Cadastrar Cliente", "Editar Cliente", "Excluir Cliente", "Listar Clientes", "Voltar ao menu anterior"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("Digite a opção desejada: ", 1, 5)
        if op == 1:
            cadastro_clientes()
        elif op == 2:
            # TODO: Chamar módulo de edição de clientes
            pass
        elif op == 3:
            # TODO: Chamar módulo de excluir clientes
            pass
        elif op == 4:
            print(f"\n {clientes}")  #Chamar módulo de listar clientes
        else:
            break
