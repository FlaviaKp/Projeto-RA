import sqlite3
import utils as u

#PROFISSIONAIS
profissionais = {}

def cadastro_profissional ():

    connection = sqlite3.connect("meu_banco.db")
    carlos = connection.cursor()

    carlos.execute("""
    CREATE TABLE IF NOT EXISTS profissionais(
                   cpf TEXT PRIMARY KEY NOT NULL,
                   nome TEXT NOT NULL,
                   area TEXT NOT NULL,
                   disponibilidade TEXT NOT NULL
    )
    """)

    print(f"\n {"-" * 10} Cadastro do Profissional {"-" * 10}")

    cpf = int(input("Informe o CPF do profissional: "))
    nome = input("Digite seu nome do profissional: ")
    area = input("Iforme sua área de atuação do profissional: ")
    disponibilidade = input("Veja a agenda do profissional: ")

    profissionais[cpf] = {
        "nome": nome,
        "cpf": cpf,
        "area": area,
        "disponibilidade": disponibilidade
    }

    carlos.execute(
        "INSERT INTO profissionais(cpf, nome, area, disponibilidade) VALUES (?,?,?,?)",
        (cpf, nome, area, disponibilidade)
    )

    connection.commit()
    connection.close()

    return

def main():
    items = ["Cadastrar Profissional", "Listar Profissinal", "Voltar ao menu anterior"]
    while True:
        u.mostrar_menu(items)
        op = u.get_int_op("Digite a opção desejada: ", 1, 3)
        if op == 1:
            cadastro_profissional()
        elif op == 2:
            print(f"\n {profissionais}")
        else:
            break
